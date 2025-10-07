from typing import Sequence

def search(parameter_one: Sequence[int]) -> int:
    answer_variable: int = -1
    variable_length: int = len(parameter_one)
    variable_maximum: int = 0
    index_counter: int = 0
    while index_counter < variable_length:
        current = parameter_one[index_counter]
        # update variable_maximum to max(variable_maximum, current)
        variable_maximum = variable_maximum if variable_maximum > current else current
        index_counter += 1

    frequency_array: list[int] = [0] * (variable_maximum + 1)

    cursor: int = 0
    while True:
        if cursor >= variable_length:
            break
        frequency_array[parameter_one[cursor]] += 1
        cursor += 1

    scan_index: int = 1
    while scan_index < len(frequency_array):
        if not frequency_array[scan_index] < scan_index:
            answer_variable = scan_index
        scan_index += 1

    return answer_variable