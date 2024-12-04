import sys

def rotations(t):
    tt = t * 2
    return [tt[i:i + len(t)] for i in range(len(t))]

def bwm(t):
    return sorted(rotations(t))

def bwtViaBwm(t):
    return ''.join(map(lambda x: x[-1], bwm(t)))

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
    result = bwtViaBwm(t)
    write_output((f"sol_q1_t{file_number}.txt"), result)

if __name__ == '__main__':
    main()