import sys
import re

def parse_input(s):
    sections = s.strip().split('--------')
    sections = [section.strip('\n') for section in sections if section.strip()]
    x = sections[0].replace(' ', '').strip()
    alphabet = sections[1].split()
    states = sections[2].split()

    T_lines = sections[3].split('\n')
    first_line = T_lines[0]
    first_line_parts = re.split(r'\s+', first_line.strip())
    if set(first_line_parts).issubset(set(states)):
        T_header = first_line_parts
        data_start_index = 1
    else:
        T_header = states
        data_start_index = 0

    T = {
        line.split()[0]: dict(zip(T_header, map(float, line.split()[1:])))
        for line in T_lines[data_start_index:]
        if line.strip()
    }

    E_lines = sections[4].split('\n')
    first_line = E_lines[0]
    first_line_parts = re.split(r'\s+', first_line.strip())
    if set(first_line_parts).issubset(set(alphabet)):
        E_header = first_line_parts
        data_start_index = 1
    else:
        E_header = alphabet
        data_start_index = 0

    E = {
        line.split()[0]: dict(zip(E_header, map(float, line.split()[1:])))
        for line in E_lines[data_start_index:]
        if line.strip()
    }

    return x, alphabet, states, T, E

def compute_forward(obs_seq, possible_states, transition_probs, emission_probs):
    seq_len = len(obs_seq)
    forward_probs = [{} for _ in range(seq_len)]
    scaling_factors = [0] * seq_len
    num_states = len(possible_states)
    initial_prob = 1.0 / num_states

    for state in possible_states:
        forward_probs[0][state] = initial_prob * emission_probs[state][obs_seq[0]]
    scaling_factors[0] = 1.0 / sum(forward_probs[0][state] for state in possible_states)
    for state in possible_states:
        forward_probs[0][state] *= scaling_factors[0]

    for time_step in range(1, seq_len):
        for curr_state in possible_states:
            forward_probs[time_step][curr_state] = (
                sum(forward_probs[time_step - 1][prev_state] * transition_probs[prev_state][curr_state] 
                    for prev_state in possible_states) 
                * emission_probs[curr_state][obs_seq[time_step]]
            )
        scaling_factors[time_step] = 1.0 / sum(forward_probs[time_step][state] for state in possible_states)
        for state in possible_states:
            forward_probs[time_step][state] *= scaling_factors[time_step]

    return forward_probs, scaling_factors

def compute_backward(obs_seq, possible_states, transition_probs, emission_probs, scaling_factors):
    seq_len = len(obs_seq)
    backward_probs = [{} for _ in range(seq_len)]

    for state in possible_states:
        backward_probs[seq_len - 1][state] = scaling_factors[seq_len - 1]

    for time_step in range(seq_len - 2, -1, -1):
        for curr_state in possible_states:
            backward_probs[time_step][curr_state] = sum(
                backward_probs[time_step + 1][next_state] 
                * transition_probs[curr_state][next_state] 
                * emission_probs[next_state][obs_seq[time_step + 1]]
                for next_state in possible_states
            )
        for state in possible_states:
            backward_probs[time_step][state] *= scaling_factors[time_step]

    return backward_probs

def compute_posterior(forward_probs, backward_probs, possible_states):
    seq_len = len(forward_probs)
    posterior_probs = [{} for _ in range(seq_len)]

    for time_step in range(seq_len):
        normalization_factor = sum(
            forward_probs[time_step][state] * backward_probs[time_step][state] 
            for state in possible_states
        )
        for state in possible_states:
            posterior_probs[time_step][state] = (
                forward_probs[time_step][state] * backward_probs[time_step][state]
            ) / normalization_factor

    return posterior_probs

def write_output(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    input_file = sys.argv[1]
    file_number = input_file.split('/')[-1][-5]

    with open(input_file, 'r') as f:
        s = f.read().strip()

    x, alphabet, states, T, E = parse_input(s)
    alpha, c = compute_forward(x, states, T, E)
    beta = compute_backward(x, states, T, E, c)
    posterior = compute_posterior(alpha, beta, states)

    output = ' '.join(states) + '\n'
    for i in range(len(x)):
        probs = [posterior[i][k] for k in states]
        output += ' '.join(map(str, probs)) + '\n'
    output = output.rstrip()

    output_file = f"sol_q3_t{file_number}.txt"
    write_output(output_file, output)