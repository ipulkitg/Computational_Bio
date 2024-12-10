import sys

def lf_mapping(bwt: str, index: int) -> int:
    sorted_bwt_column = ''.join(sorted(bwt))
    last_column_char_counts = {}
    first_column_char_counts = {}
    last_column_occurrences = [] 
    first_column_occurrences = []
    
    for char in bwt:
        if char not in last_column_char_counts:
            last_column_char_counts[char] = 0
        last_column_occurrences.append(last_column_char_counts[char])
        last_column_char_counts[char] += 1
    
    for char in sorted_bwt_column:
        if char not in first_column_char_counts:
            first_column_char_counts[char] = 0
        first_column_occurrences.append(first_column_char_counts[char])
        first_column_char_counts[char] += 1

    char_at_index = bwt[index]
    occurrence_index = last_column_occurrences[index]
    
    for i, (char, occ) in enumerate(zip(sorted_bwt_column, first_column_occurrences)):
        if char == char_at_index and occ == occurrence_index:
            return i
    
    return -1

def read_input(input_filename):
    with open(input_filename, 'r') as file:
        lines = file.readlines()
        t = lines[0].strip()
        index = int(lines[1].strip())
    return t,index

def write_output(output_filename, result):
    with open(output_filename, 'w') as file:
        file.write(result)


def main():
    file_path = sys.argv[1]
    file_number = file_path.split('/')[-1][-5]
    t,index = read_input(file_path)
    result = str(lf_mapping(t,index))
    write_output((f"sol_q3_t{file_number}.txt"), result)

if __name__ == '__main__':
    main()