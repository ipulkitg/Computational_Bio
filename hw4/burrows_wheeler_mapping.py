import sys

def find_bwt_matching(bwt, patterns):
    bwt_length = len(bwt)
    first_column = sorted(bwt)
    unique_chars = sorted(set(bwt))
    char_counts = {char: 0 for char in unique_chars}
    for char in bwt:
        char_counts[char] += 1

    char_start_positions = {}  
    cumulative_count = 0       
    for char in unique_chars:
        char_start_positions[char] = cumulative_count
        cumulative_count += char_counts[char]

    occurrence_table = {char: [0] * (bwt_length + 1) for char in unique_chars}
    for i in range(1, bwt_length + 1):
        current_char = bwt[i - 1]
        for char in unique_chars:
            occurrence_table[char][i] = occurrence_table[char][i - 1]
        occurrence_table[current_char][i] += 1


    def count_pattern_occurrences(pattern):
        top = 0
        bottom = bwt_length - 1
        while top <= bottom and pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in unique_chars:
                top = char_start_positions[symbol] + occurrence_table[symbol][top]
                bottom = char_start_positions[symbol] + occurrence_table[symbol][bottom + 1] - 1
            else:
                return 0
        if top > bottom:
            return 0
        else:
            return bottom - top + 1
    pattern_match_counts = []
    for pattern in patterns:
        match_count = count_pattern_occurrences(pattern)
        pattern_match_counts.append(str(match_count))

    return ' '.join(pattern_match_counts)

def read_input(input_filename):
    with open(input_filename, 'r') as file:
        lines = file.readlines()
        t = lines[0].strip()
        pattern = str(lines[1].strip())
        pattern = pattern.split()
        return t,pattern

def write_output(output_filename, result):
    with open(output_filename, 'w') as file:
        file.write(result)


def main():
    file_path = sys.argv[1]
    file_number = file_path.split('/')[-1][-5]
    t,pattern = read_input(file_path)
    result = str(find_bwt_matching(t,pattern))
    write_output((f"sol_q4_t{file_number}.txt"), result)

if __name__ == '__main__':
    main()