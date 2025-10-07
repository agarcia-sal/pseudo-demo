from typing import Tuple

def reverse_delete(str_input: str, filter_string: str) -> Tuple[str, bool]:
    filtered_result = []
    position = 0
    while position < len(str_input):
        current_char = str_input[position]
        if current_char not in filter_string:
            filtered_result.append(current_char)
        position += 1
    filtered_str = ''.join(filtered_result)
    reversed_check = True
    left_index = 0
    right_index = len(filtered_str) - 1
    while left_index < right_index:
        if filtered_str[left_index] != filtered_str[right_index]:
            reversed_check = False
            break
        left_index += 1
        right_index -= 1
    return filtered_str, reversed_check