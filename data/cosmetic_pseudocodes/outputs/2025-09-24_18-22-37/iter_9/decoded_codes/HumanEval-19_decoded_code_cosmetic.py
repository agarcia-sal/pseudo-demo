from typing import Dict


def sort_numbers(input_string: str) -> str:
    mapping_dictionary: Dict[str, int] = {
        'zero': 0,
        'one': 0 + 1,
        'two': 1 + 1,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    temporary_list = [token for token in input_string.split(' ') if token != '']
    secondary_list = temporary_list
    for index_var in range(len(secondary_list) - 1, 0, -1):
        for inner_index in range(index_var):
            first_value = mapping_dictionary[secondary_list[inner_index]]
            second_value = mapping_dictionary[secondary_list[inner_index + 1]]
            if not (first_value <= second_value):
                # Swap elements if out of order
                secondary_list[inner_index], secondary_list[inner_index + 1] = (
                    secondary_list[inner_index + 1],
                    secondary_list[inner_index],
                )
    result_string = ''
    for position_var in range(len(secondary_list) - 1):
        result_string += secondary_list[position_var] + ' '
    result_string += secondary_list[len(secondary_list) - 1]
    return result_string