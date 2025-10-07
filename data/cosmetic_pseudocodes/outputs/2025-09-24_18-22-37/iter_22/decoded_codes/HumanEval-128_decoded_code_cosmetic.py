from typing import Sequence, Optional

def prod_signs(sequence_of_numbers: Sequence[int]) -> Optional[int]:
    index_counter: int = 0
    has_zero: bool = False
    negatives_count: int = 0
    total_magnitude: int = 0
    product_sign: int = 0

    while index_counter < len(sequence_of_numbers):
        current_element: int = sequence_of_numbers[index_counter]
        if current_element == 0:
            has_zero = True
        else:
            if current_element < 0:
                negatives_count += 1
        # Add magnitude of current element to total_magnitude
        total_magnitude += (-current_element) * (current_element < 0) + current_element * (not (current_element < 0))
        index_counter += 1

    if len(sequence_of_numbers) == 0:
        return None

    if has_zero:
        product_sign = 0
    else:
        power_value: int = 1
        exponent: int = 0
        while exponent < negatives_count:
            power_value *= -1
            exponent += 1
        product_sign = power_value

    return product_sign * total_magnitude