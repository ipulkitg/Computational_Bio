import random
import sys
import re
import os

def input_parser(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()  
    k, t, N = map(int, lines[0].split())  
    Dna = lines[1:] 
    return k, t, N, Dna

def BuildProfileWithPseudocounts(motifs):
    t = len(motifs)
    k = len(motifs[0])
    # Initialize profile with pseudocounts of 1
    profile = {nucleotide: [1] * k for nucleotide in 'ACGT'}
    for motif in motifs:
        for i, nucleotide in enumerate(motif):
            profile[nucleotide][i] += 1
    for nucleotide in profile:
        profile[nucleotide] = [count / (t + 4) for count in profile[nucleotide]]  
    return profile

def CalculateProbability(text, profile):
    prob = 1.0
    for i, nucleotide in enumerate(text):
        prob *= profile[nucleotide][i]
    return prob

def GenerateProfileRandomlyGeneratedKmer(text, k, profile):
    n = len(text)
    probabilities = []
    for i in range(n - k + 1):
        kmer = text[i:i+k]
        probabilities.append(CalculateProbability(kmer, profile))
    total_prob = sum(probabilities)
    probabilities = [p / total_prob for p in probabilities]
    i = random.choices(range(n - k + 1), weights=probabilities)[0]
    return text[i:i+k]

def CalculateMotifScore(motifs):
    total_score = 0
    k = len(motifs[0])
    
    for i in range(k):
        counts = {'A':0, 'C':0, 'G':0, 'T':0}
        
        # Count nucleotides at the current position in all motifs
        for motif in motifs:
            counts[motif[i]] += 1
        
        # Add the score for the current position
        total_score += len(motifs) - max(counts.values())
    
    return total_score

def SampleMotifsUsingGibbs(Dna, k, t, N):
    motifs = [random.choice([dna[i:i+k] for i in range(len(dna)-k+1)]) for dna in Dna]
    best_motifs = motifs[:]
    best_score = CalculateMotifScore(motifs)
    for j in range(N):
        i = random.randint(0, t-1)
        motifs_except_i = motifs[:i] + motifs[i+1:]
        profile = BuildProfileWithPseudocounts(motifs_except_i)
        motifs[i] = GenerateProfileRandomlyGeneratedKmer(Dna[i], k, profile)
        current_score = CalculateMotifScore(motifs)
        if current_score < best_score:
            best_motifs = motifs[:]
            best_score = current_score
    return best_motifs

def RunGibbsSampler(Dna, k, t, N, times=30):
    best_motifs = None
    best_score = float('inf')
    for _ in range(times):
        motifs = SampleMotifsUsingGibbs(Dna, k, t, N)
        current_score = CalculateMotifScore(motifs)
        if current_score < best_score:
            best_motifs = motifs
            best_score = current_score
    return best_motifs

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 q2.py test_{i}.txt")
        sys.exit(1)
    input_file = sys.argv[1]
    # Extract test case number from input filename
    base_filename = os.path.basename(input_file)  # Get the base filename without the path
    match = re.match(r'test_(\d+)\.txt', base_filename)
    if not match:
        print("Input filename must be in the format test_{i}.txt")
        sys.exit(1)
    testcase_num = match.group(1)
    question_num = '2'  # Since the script is q2.py, question number is 2

    k, t, N, Dna = input_parser(input_file)
    best_motifs = RunGibbsSampler(Dna, k, t, N, times=30)

    # Write output to the appropriate file
    output_filename = f"sol_q{question_num}_t{testcase_num}.txt"
    with open(output_filename, 'w') as f:
        for motif in best_motifs:
            f.write(f"{motif}\n")

if __name__ == "__main__":
    main()