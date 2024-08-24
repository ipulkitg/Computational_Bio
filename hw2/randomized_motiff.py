import random
import sys
import re
import os


def input_parser(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
    k, t = map(int, lines[0].split())
    dna = [line.strip() for line in lines[1:]]
    return k, t, dna

def CalculateMotifScore(motifs):
    total_score = 0
    consensus = ""
    k = len(motifs[0])
    for i in range(k):
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            count[motif[i]] += 1
        consensus += max(count, key=count.get)
        total_score += sum(count[base] for base in "ACGT" if base != consensus[-1])
    return total_score

def BuildProfileWithPseudocounts(motifs):
    profile = {'A': [], 'C': [], 'G': [], 'T': []}
    k = len(motifs[0])
    t = len(motifs)
    for i in range(k):
        count = {'A': 1, 'C': 1, 'G': 1, 'T': 1}  # Pseudocounts
        for motif in motifs:
            count[motif[i]] += 1
        for base in "ACGT":
            profile[base].append(count[base] / (t + 4))  # Normalize
    return profile

def most_probable_kmer(dna, k, profile):
    most_prob_kmer = dna[:k]
    max_prob = -1
    
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i+k]
        prob = prod(profile[base][j] for j, base in enumerate(kmer))
        
        if prob > max_prob:
            max_prob = prob
            most_prob_kmer = kmer

    return most_prob_kmer

def prod(iterable):
    result = 1
    for x in iterable:
        result *= x
    return result

def randomized_motif_search(dna, k, t):
    motifs = [random.choice([dna[i][j:j+k] for j in range(len(dna[i]) - k + 1)]) for i in range(t)]
    best_motifs = motifs[:]
    while True:
        profile = BuildProfileWithPseudocounts(motifs)
        motifs = [most_probable_kmer(dna[i], k, profile) for i in range(t)]
        if CalculateMotifScore(motifs) < CalculateMotifScore(best_motifs):
            best_motifs = motifs[:]
        else:
            return best_motifs

def run_randomized_motif_search(file_name, iterations=1500):
    k, t, dna = input_parser(file_name)
    best_motifs = None
    for _ in range(iterations):
        motifs = randomized_motif_search(dna, k, t)
        if best_motifs is None or CalculateMotifScore(motifs) < CalculateMotifScore(best_motifs):
            best_motifs = motifs
    return best_motifs

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python3 q1.py test_i.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    # Extract filename from input_file
    input_filename = os.path.basename(input_file)
    # Extract test case number from input filename
    match = re.match(r'test_(\d+)\.txt', input_filename)
    if not match:
        print("Input file name must be of the format test_i.txt")
        sys.exit(1)
    test_case_num = match.group(1)
    question_num = 1  # Assuming this is question 1

    output_file = f'sol_q{question_num}_t{test_case_num}.txt'

    best_motifs = run_randomized_motif_search(input_file)
    # Write output to the output file
    with open(output_file, 'w') as f:
        f.write('\n'.join(best_motifs))