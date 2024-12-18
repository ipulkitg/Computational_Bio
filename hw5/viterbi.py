import sys

def read_input(filename):
    with open(filename, 'r') as f:
        x = f.readline().strip()
        f.readline()

        sigma_line = f.readline().strip()
        sigma = sigma_line.split()
        f.readline()

        states_line = f.readline().strip()
        states = states_line.split()
        f.readline()

        header_line = f.readline().strip()
        headers = header_line.split()
        T = {}
        for _ in states:
            line = f.readline().strip()
            tokens = line.split()
            row_state = tokens[0]
            probs = list(map(float, tokens[1:]))
            T[row_state] = dict(zip(headers, probs))
        f.readline()

        header_line = f.readline().strip()
        symbols = header_line.split()
        E = {}
        for _ in states:
            line = f.readline().strip()
            tokens = line.split()
            row_state = tokens[0]
            probs = list(map(float, tokens[1:]))
            E[row_state] = dict(zip(symbols, probs))

        return x, sigma, states, T, E
    
def viterbi(x, states, T, E):
    n = len(x)
    V = [{}]
    path = {}

    # Initialize base cases (t == 0)
    for s in states:
        V[0][s] = (1.0 / len(states)) * E[s][x[0]]
        path[s] = [s]

    # Run Viterbi for t > 0
    for t in range(1, n):
        V.append({})
        new_path = {}

        for curr_state in states:
            max_prob = -1
            max_state = None
            for prev_state in states:
                prob = V[t-1][prev_state] * T[prev_state][curr_state] * E[curr_state][x[t]]
                if prob > max_prob:
                    max_prob = prob
                    max_state = prev_state
            V[t][curr_state] = max_prob
            new_path[curr_state] = path[max_state] + [curr_state]
        # Update path
        path = new_path

    # Find the final most probable state
    max_prob = -1
    max_state = None
    n -= 1
    for s in states:
        if V[n][s] > max_prob:
            max_prob = V[n][s]
            max_state = s
    return ''.join(path[max_state])

def write_output(output_filename, result):
    with open(output_filename, 'w') as file:
        file.write(result)

# Main execution
def main():
    file_path = sys.argv[1]
    file_number = file_path.split('/')[-1][-5]
    x, sigma, states, T, E = read_input(file_path)
    most_probable_path = viterbi(x, states, T, E)
    write_output((f"sol_q1_t{file_number}.txt"), most_probable_path)

if __name__ == "__main__":
    main()