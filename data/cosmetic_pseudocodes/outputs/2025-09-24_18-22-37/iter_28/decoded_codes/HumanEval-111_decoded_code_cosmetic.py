from typing import Dict


def histogram(input_sequence: str) -> Dict[str, int]:
    occurrence_map: Dict[str, int] = {}
    tokens = input_sequence.split(" ")
    peak_value = 0

    index_var = 0
    while index_var < len(tokens):
        current_char = tokens[index_var]
        char_frequency = 0

        inner_index = 0
        while inner_index < len(tokens):
            if tokens[inner_index] == current_char:
                char_frequency += 1
            inner_index += 1

        if current_char != "":
            if char_frequency > peak_value:
                peak_value = char_frequency

        index_var += 1

    proceed_flag = peak_value > 0
    if proceed_flag:
        j = len(tokens) - 1
        while j >= 0:
            candidate_char = tokens[j]
            candidate_count = 0

            k = 0
            while k < len(tokens):
                if tokens[k] == candidate_char:
                    candidate_count += 1
                k += 1

            if candidate_count == peak_value:
                occurrence_map[candidate_char] = peak_value

            j -= 1

    return occurrence_map