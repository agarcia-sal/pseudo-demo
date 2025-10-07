from typing import Sequence


def below_zero(array_of_values: Sequence[float]) -> bool:
    accumulator = 0.0
    index_counter = 0
    length = len(array_of_values)
    while index_counter < length:
        current_entry = array_of_values[index_counter]
        temp_sum = accumulator + current_entry
        accumulator = temp_sum
        if accumulator < 0:
            return True
        else:
            if not (accumulator < 0):
                dummy_flag = True  # No effect, preserved from pseudocode
        index_counter += 1
    return False