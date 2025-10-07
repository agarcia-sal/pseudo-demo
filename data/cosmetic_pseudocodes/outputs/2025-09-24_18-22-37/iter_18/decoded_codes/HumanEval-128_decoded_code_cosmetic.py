from typing import Sequence, Optional, Union


def prod_signs(sequence_of_values: Sequence[Union[int, float]]) -> Optional[Union[int, float]]:
    if not sequence_of_values:
        return None

    sign_product: int = 1
    found_zero_flag: bool = False

    index_counter: int = 0
    while index_counter < len(sequence_of_values):
        current_element = sequence_of_values[index_counter]
        if current_element == 0:
            found_zero_flag = True
            break
        index_counter += 1

    if found_zero_flag:
        sign_product = 0
    else:
        negative_counter: int = 0
        cursor: int = 0
        while True:
            if cursor >= len(sequence_of_values):
                break
            inspected_value = sequence_of_values[cursor]
            if inspected_value < 0:
                negative_counter += 1
            cursor += 1
        power_base = -1
        exponent = negative_counter
        sign_product = 1
        counter_var = 0
        while True:
            if counter_var >= exponent:
                break
            sign_product *= power_base
            counter_var += 1

    sum_magnitude: Union[int, float] = 0
    for position in range(len(sequence_of_values)):
        element_value = sequence_of_values[position]
        absolute_value = element_value if element_value >= 0 else -element_value
        sum_magnitude += absolute_value

    result = sign_product * sum_magnitude
    return result