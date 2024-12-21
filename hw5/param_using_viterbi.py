import sys
import os
import math

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
    transitions_raw = sections[4].splitlines()
    transition_states = transitions_raw[0].split()
    transition_matrix = {
        row.split()[0]: dict(zip(transition_states, map(float, row.split()[1:])))
        for row in transitions_raw[1:]
    }
    emissions_raw = sections[5].splitlines()
    emission_symbols = emissions_raw[0].split()
    emission_matrix = {
        row.split()[0]: dict(zip(emission_symbols, map(float, row.split()[1:])))
        for row in emissions_raw[1:]
    }
    return [num_iterations, observed_sequence, alphabet, states, transition_matrix, emission_matrix]

def viterbi_algorithm(observation_seq, possible_states, initial_probabilities, transition_probs, emission_probs):
    sequence_length, num_states = len(observation_seq), len(possible_states)
    paths, probabilities = {}, [{}]

    # Base case t == 0
    for curr_state in possible_states:
        init_prob = initial_probabilities[curr_state]
        emit_prob = emission_probs[curr_state][observation_seq[0]]
        probabilities[0][curr_state] = (
            math.log(init_prob) + math.log(emit_prob)
            if init_prob > 0 and emit_prob > 0 else float('-inf')
        )
        paths[curr_state] = [curr_state]
    
    # Viterbi for t > 0
    for time_step in range(1, sequence_length):
        probabilities.append({})
        new_paths = {}
        for next_state in possible_states:
            transition_items = [
                (
                    probabilities[time_step - 1][prev_state] + 
                    math.log(transition_probs[prev_state][next_state]) + 
                    math.log(emission_probs[next_state][observation_seq[time_step]])
                    if transition_probs[prev_state][next_state] > 0 and 
                       emission_probs[next_state][observation_seq[time_step]] > 0 else float('-inf'),
                    prev_state
                )
                for prev_state in possible_states
            ]
            max_prob, best_prev_state = max(transition_items)
            probabilities[time_step][next_state] = max_prob
            new_paths[next_state] = paths[best_prev_state] + [next_state]
        paths = new_paths
    
    final_step = sequence_length - 1
    _, best_final_state = max(
        (probabilities[final_step][state], state) for state in possible_states
    )
    return paths[best_final_state]

def reestimate_parameters(obs_seq, possible_states, symbols, viterbi_path):
    transition_counts = {state: {next_state: 0 for next_state in possible_states} for state in possible_states}
    emission_counts = {state: {symbol: 0 for symbol in symbols} for state in possible_states}
    state_counts = {state: 0 for state in possible_states}
    
    for t, (curr_state, curr_symbol) in enumerate(zip(viterbi_path, obs_seq)):
        emission_counts[curr_state][curr_symbol] += 1
        state_counts[curr_state] += 1
        if t > 0:
            transition_counts[viterbi_path[t - 1]][curr_state] += 1

    transition_matrix = {
        state_from: {
            state_to: (
                transition_counts[state_from][state_to] / total_transitions
                if total_transitions > 0 else 1.0 / len(possible_states)
            )
            for state_to in possible_states
        }
        for state_from, total_transitions in ((state, sum(transition_counts[state].values())) for state in possible_states)
    }

    emission_matrix = {
        state: {
            symbol: (
                emission_counts[state][symbol] / total_emissions
                if total_emissions > 0 else 1.0 / len(symbols)
            )
            for symbol in symbols
        }
        for state, total_emissions in ((state, state_counts[state]) for state in possible_states)
    }
    
    return [transition_matrix, emission_matrix]

def viterbi_learning(num_iterations, observed_sequence, alphabet, states, transition_matrix, emission_matrix):
    start_prob = {state: 1.0 / len(states) for state in states}
    
    for _ in range(num_iterations):
        viterbi_path = viterbi_algorithm(observed_sequence, states, start_prob, transition_matrix, emission_matrix)
        transition_matrix, emission_matrix = reestimate_parameters(observed_sequence, states, alphabet, viterbi_path)

    return [transition_matrix, emission_matrix]

def format_output(states, transition_matrix, alphabet, emission_matrix):
    def format_matrix(matrix, row_headers, col_headers):
        header = '\t'.join(col_headers) + '\n'
        rows = []
        for row_header in row_headers:
            row = [row_header] + [f"{round(matrix[row_header][col_header], 3)}" for col_header in col_headers]
            rows.append('\t'.join(row))
        return header + '\n'.join(rows)

    output = format_matrix(transition_matrix, states, states) + '\n--------\n'
    output += format_matrix(emission_matrix, states, alphabet)

    return output

def write_output(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    input_file = sys.argv[1]
    file_number = input_file.split('/')[-1][-5]
    sections = parse_input_file(input_file)
    num_iterations, observed_sequence, alphabet, states, transition_matrix, emission_matrix = initialize_parameters(sections)
    transition_matrix, emission_matrix = viterbi_learning(num_iterations, observed_sequence, alphabet, states, transition_matrix, emission_matrix)
    output = format_output(states, transition_matrix, alphabet, emission_matrix)
    output_file = f"sol_q2_t{file_number}.txt"
    write_output(output_file, output)