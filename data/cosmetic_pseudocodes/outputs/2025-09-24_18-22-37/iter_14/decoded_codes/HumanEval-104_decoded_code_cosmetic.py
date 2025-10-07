from typing import List


def unique_digits(array_of_numbers: List[int]) -> List[int]:
    collected_odds: List[int] = []
    idx: int = 0
    while idx < len(array_of_numbers):
        current_val: int = array_of_numbers[idx]
        digits_collection: List[int] = []
        temp_val: int = current_val
        while temp_val > 0:
            digit_extracted: int = temp_val % 10
            temp_val //= 10
            digits_collection.append(digit_extracted)
        all_odd_flag: bool = True
        digit_ptr: int = 0
        while digit_ptr < len(digits_collection):
            examined_digit: int = digits_collection[digit_ptr]
            if examined_digit % 2 == 0:
                all_odd_flag = False
                break
            digit_ptr += 1
        if all_odd_flag:
            collected_odds.append(current_val)
        idx += 1
    sorted_collection: List[int] = sorted(collected_odds)
    return sorted_collection