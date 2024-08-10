import os
import sys

# Function to process the text (you can modify this function as needed)
def calculate_z(s):
    Z = [0] * len(s)
    left, right = 0, 0
    comparisons = 0  # Count of real character comparisons
    matches = 0  # Count of successful character comparisons
    mismatches = 0  # Count of unsuccessful character comparisons (mismatches)
    
    for i in range(1, len(s)):
        if i > right:
            # Case 1: We're outside the Z-box, so calculate Z[i] from scratch
            left, right = i, i
            while right < len(s) and s[right] == s[right - left]:
                comparisons += 1  
                matches += 1  
                right += 1
            if right < len(s) and s[right] != s[right - left]:
                comparisons += 1  
                mismatches += 1 
            Z[i] = right - left
            right -= 1
        else:
            # Inside Z-box
            K = i - left
            if Z[K] < right - i + 1:
                Z[i] = Z[K]  # No new comparisons, reuse the Z-box
            else:
                # Carefully extend the Z-box only if absolutely necessary
                left = i
                right += 1

                # Extend the Z-box only as long as characters match
                while right < len(s) and s[right] == s[right - left]:
                    comparisons += 1  
                    matches += 1  
                    right += 1
                if right < len(s) and s[right] != s[right - left]:
                    comparisons += 1  
                    mismatches += 1 
                Z[i] = right - left
                right -= 1

    return Z, comparisons, matches, mismatches

def z_algorithm_pattern_matching(t, p):
    # Concatenate pattern, separator, and text
    concat = p + "$" + t
    Z, comparisons, matches, mismatches = calculate_z(concat)
    
    # Length of pattern
    pattern_length = len(p)
    
    # Find all occurrences of pattern in text
    occurrences = []
    for i in range(pattern_length + 1, len(Z)):
        if Z[i] == pattern_length:
            occurrences.append(i - pattern_length)  # Adjust to 1-based index
    
    return occurrences, comparisons, matches, mismatches

def process_file(input_file):
    # Read input file
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            text = lines[0].strip()
            pattern = lines[1].strip()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    # Process the text
    occurrences, comparisons, matches, mismatches = z_algorithm_pattern_matching(text, pattern)
    
    # Ensure the 'solutions' directory exists
    solutions_dir = "solutions"
    if not os.path.exists(solutions_dir):
        os.makedirs(solutions_dir)

    processed_text = ""
    for pos in occurrences:
        processed_text += f"{pos}\n"
    processed_text += f"Number of comparisons: {comparisons}\n"
    processed_text += f"Number of matches: {matches}\n"
    processed_text += f"Number of mismatches: {mismatches}\n"

     # Modify the output file name based on input file name
    base_name = os.path.basename(input_file)  # Get the base name of the file
    file_name, ext = os.path.splitext(base_name)  # Split the name and extension

    if "sample" in file_name:
        output_file_name = file_name.replace("sample", "sol") + ext
    else:
        output_file_name = file_name + "_sol" + ext

    # Define the output file path in the solutions directory
    output_file = os.path.join(solutions_dir, output_file_name)

    # Write the processed text to the output file
    with open(output_file, 'w') as file:
        file.write(processed_text)

    print(f"Processed file saved at: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_text_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    process_file(input_file)