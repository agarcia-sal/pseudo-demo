from typing import Sequence, List


def unique_digits(sequence_of_positive_numbers: Sequence[int]) -> List[int]:
    collected_odd_digit_values: List[int] = []
    current_index: int = 0
    while current_index < len(sequence_of_positive_numbers):
        number_value: int = sequence_of_positive_numbers[current_index]
        digit_index: int = 0
        contains_even_digit: bool = False
        number_str: str = str(number_value)
        while digit_index < len(number_str):
            single_digit: int = int(number_str[digit_index])
            if single_digit % 2 == 0:
                contains_even_digit = True
            digit_index += 1
        if not contains_even_digit:
            collected_odd_digit_values.append(number_value)
        current_index += 1
    return sorted(collected_odd_digit_values)