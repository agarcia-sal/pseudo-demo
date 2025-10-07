from typing import List, Dict

def sort_numbers(original_sequence: str) -> str:
    digit_values: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 1 + 1,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    intermediate_list: List[str] = []
    tokens = original_sequence.split(' ')
    index_counter = 0
    while index_counter < len(tokens):
        current_candidate = tokens[index_counter]
        if current_candidate != '':
            intermediate_list.append(current_candidate)
        index_counter += 1

    for i in range(len(intermediate_list) - 1):
        outer_idx = i
        j = i + 1
        while j < len(intermediate_list):
            left_word = intermediate_list[outer_idx]
            right_word = intermediate_list[j]
            left_val = digit_values[left_word]
            right_val = digit_values[right_word]
            if not (left_val <= right_val):
                intermediate_list[outer_idx], intermediate_list[j] = intermediate_list[j], intermediate_list[outer_idx]
            j += 1

    join_index = 0
    result_string = ''
    while join_index < len(intermediate_list):
        element_to_add = intermediate_list[join_index]
        if join_index == 0:
            result_string = element_to_add
        else:
            result_string += ' ' + element_to_add
        join_index += 1

    return result_string