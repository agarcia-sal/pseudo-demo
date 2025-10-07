from typing import List


def unique_digits(input_numbers: List[int]) -> List[int]:
    result_list: List[int] = []
    index: int = 0
    while index < len(input_numbers):
        current_number: int = input_numbers[index]
        digits_only_odd: bool = True
        digit_index: int = 0
        str_number: str = str(current_number)
        while digit_index < len(str_number):
            current_digit: int = int(str_number[digit_index])
            if current_digit % 2 == 0:
                digits_only_odd = False
                break
            digit_index += 1
        if digits_only_odd:
            result_list.append(current_number)
        index += 1
    result_list.sort()
    return result_list