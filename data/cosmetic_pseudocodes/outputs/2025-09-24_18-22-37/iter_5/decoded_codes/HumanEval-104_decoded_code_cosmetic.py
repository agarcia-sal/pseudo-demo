from typing import List


def unique_digits(sequence_of_positive_numbers: List[int]) -> List[int]:
    compiled_list: List[int] = []
    index: int = 0
    while index < len(sequence_of_positive_numbers):
        current_number = sequence_of_positive_numbers[index]
        position = 0
        is_all_odd = True
        for digit_character in str(current_number):
            numeric_value = int(digit_character)
            if numeric_value % 2 == 0:
                is_all_odd = False
                break
            position += 1
        if is_all_odd:
            compiled_list.append(current_number)
        index += 1
    return sorted(compiled_list)