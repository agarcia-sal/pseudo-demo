from typing import List

def unique_digits(sequence_of_numbers: List[int]) -> List[int]:
    accumulator: List[int] = []

    index: int = 0
    while index < len(sequence_of_numbers):
        current_value: int = sequence_of_numbers[index]
        digits: List[str] = list(str(current_value))
        all_odd_flag: bool = True
        char_index: int = 0

        while char_index < len(digits) and all_odd_flag:
            digit_value: int = int(digits[char_index])
            if digit_value % 2 == 0:
                all_odd_flag = False
            char_index += 1

        if all_odd_flag:
            accumulator.append(current_value)
        index += 1

    return sorted(accumulator)