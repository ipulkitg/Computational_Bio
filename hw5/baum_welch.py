import sys

def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    sections = data.split('--------\n')
    return [section.strip() for section in sections if section.strip()]


def initialize_parameters(sections):
    num_iterations = int(sections[0])
    observed_sequence = sections[1]
    alphabet = sections[2].split()
    states = sections[3].split()
    
    # Parse transition matrix
    transitions_raw = sections[4].splitlines()
    transition_matrix = {}
    for row in transitions_raw[1:]:
        items = row.split()
        state = items[0]
        transition_matrix[state] = list(map(float, items[1:]))
    
    # Parse emission matrix
    emissions_raw = sections[5].splitlines()
    emission_matrix = {}
    for row in emissions_raw[1:]:
        items = row.split()
        state = items[0]
        emission_matrix[state] = list(map(float, items[1:]))
    
    return num_iterations, observed_sequence, alphabet, states, transition_matrix, emission_matrix


def baum_welch(num_iterations, observed_sequence, alphabet, states, transition_matrix, emission_matrix):
    # Initialize required variables
    n = len(states)
    m = len(alphabet)
    T = len(observed_sequence)
    
    for _ in range(num_iterations):
        # Expectation step: Calculate forward and backward probabilities
        forward = [{} for _ in range(T)]
        backward = [{} for _ in range(T)]
        
        # Forward algorithm
        for t in range(T):
            symbol = observed_sequence[t]
            for state in states:
                if t == 0:
                    forward[t][state] = emission_matrix[state][alphabet.index(symbol)]
                else:
                    forward[t][state] = sum(
                        forward[t-1][prev_state] * transition_matrix[prev_state][states.index(state)]
                        for prev_state in states
                    ) * emission_matrix[state][alphabet.index(symbol)]
        
        # Backward algorithm
        for t in reversed(range(T)):
            symbol = observed_sequence[t]
            for state in states:
                if t == T - 1:
                    backward[t][state] = 1
                else:
                    backward[t][state] = sum(
                        backward[t+1][next_state] *
                        transition_matrix[state][states.index(next_state)] *
                        emission_matrix[next_state][alphabet.index(observed_sequence[t+1])]
                        for next_state in states
                    )
        
        # Update step: Soft decoding
        gamma = [{} for _ in range(T)]
        xi = [{} for _ in range(T - 1)]
        
        for t in range(T):
            total = sum(forward[t][state] * backward[t][state] for state in states)
            for state in states:
                gamma[t][state] = (forward[t][state] * backward[t][state]) / total
        
        for t in range(T - 1):
            total = 0
            for state in states:
                for next_state in states:
                    total += (
                        forward[t][state] *
                        transition_matrix[state][states.index(next_state)] *
                        emission_matrix[next_state][alphabet.index(observed_sequence[t+1])] *
                        backward[t+1][next_state]
                    )
            for state in states:
                xi[t][state] = {}
                for next_state in states:
                    xi[t][state][next_state] = (
                        forward[t][state] *
                        transition_matrix[state][states.index(next_state)] *
                        emission_matrix[next_state][alphabet.index(observed_sequence[t+1])] *
                        backward[t+1][next_state]
                    ) / total
        
        # Update transition and emission matrices
        for state in states:
            for next_state in states:
                numerator = sum(xi[t][state][next_state] for t in range(T - 1))
                denominator = sum(gamma[t][state] for t in range(T - 1))
                transition_matrix[state][states.index(next_state)] = numerator / denominator
            
            for symbol in alphabet:
                numerator = sum(
                    gamma[t][state]
                    for t in range(T)
                    if observed_sequence[t] == symbol
                )
                denominator = sum(gamma[t][state] for t in range(T))
                emission_matrix[state][alphabet.index(symbol)] = numerator / denominator
    
    return transition_matrix, emission_matrix


def format_matrix(matrix, row_headers, col_headers):
    """
    Formats a matrix (dictionary of dictionaries) for writing to a file.
    """
    output = '\t'.join(col_headers) + '\n'
    for row_header in row_headers:
        row = [row_header] + [f'{matrix[row_header][col_header]:.3f}' for col_header in col_headers]
        output += '\t'.join(row) + '\n'
    return output

def write_output_to_file(file_name, alphabet, states, transition_matrix, emission_matrix):
    with open(file_name, 'w') as file:
        # Write transition matrix header
        file.write("\t" + "\t".join(states) + "\n")
        for state, row in transition_matrix.items():
            file.write(f"{state}\t" + "\t".join(f"{val:.3f}" for val in row) + "\n")
        file.write("--------\n")
        
        # Write emission matrix header
        file.write("\t" + "\t".join(alphabet) + "\n")
        for state, row in emission_matrix.items():
            file.write(f"{state}\t" + "\t".join(f"{val:.3f}" for val in row) + "\n")


def main():
    file_path = sys.argv[1]
    file_number = file_path.split('/')[-1][-5]
    sections = parse_input_file(file_path)
    # Initialize parameters
    num_iterations, observed_sequence, alphabet, states, transition_matrix, emission_matrix = initialize_parameters(sections)
    # Run Baum-Welch
    updated_transition_matrix, updated_emission_matrix = baum_welch(
        num_iterations, observed_sequence, alphabet, states, transition_matrix, emission_matrix
    )
    
    write_output_to_file((f"sol_q4_t{file_number}.txt"),alphabet, states, updated_transition_matrix, updated_emission_matrix)

if __name__ == "__main__":
    main()