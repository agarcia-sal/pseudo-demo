from typing import List


def separate_paren_groups(operand_string: str) -> List[str]:
    accumulator_results: List[str] = []
    buffer_string: List[str] = []
    counter_depth_var: int = 0

    iterator_index: int = 0
    length: int = len(operand_string)
    while iterator_index < length:
        current_char: str = operand_string[iterator_index]

        if current_char != ')':
            if current_char == '(':
                counter_depth_var += 1
                buffer_string.append(current_char)
        else:
            buffer_string.append(current_char)
            counter_depth_var -= 1
            if counter_depth_var == 0:
                joined_buffer = ''.join(buffer_string)
                accumulator_results.append(joined_buffer)
                buffer_string.clear()

        iterator_index += 1

    return accumulator_results