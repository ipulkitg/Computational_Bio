import sys

def reverse_bwt(bwt):
    table = [""] * len(bwt)
    
    for _ in range(len(bwt)):
        table = sorted([bwt[i] + table[i] for i in range(len(bwt))])
    
    for row in table:
        if row.endswith('$'):
            return row

def read_input(input_filename):
    with open(input_filename, 'r') as file:
        lines = file.readlines()
        t = lines[0].strip()
    return t

def write_output(output_filename, result):
    with open(output_filename, 'w') as file:
        file.write(result)


def main():
    file_path = sys.argv[1]
    file_number = file_path.split('/')[-1][-5]
    t = read_input(file_path)
    result = reverse_bwt(t)
    write_output((f"sol_q2_t{file_number}.txt"), result)

if __name__ == '__main__':
    main()