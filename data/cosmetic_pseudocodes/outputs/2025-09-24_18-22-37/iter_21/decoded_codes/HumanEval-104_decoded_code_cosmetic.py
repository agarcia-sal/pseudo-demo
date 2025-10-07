from typing import List

def unique_digits(chosen_numbers: List[int]) -> List[int]:
    odd_number_collection: List[int] = []
    for candidate in chosen_numbers:
        digit_index = 1
        all_odd_flag = True
        while True:
            current_digit = (candidate // digit_index) % 10
            if current_digit % 2 == 0:
                all_odd_flag = False
                break
            digit_index *= 10
            if candidate // digit_index == 0 or not all_odd_flag:
                break
        if all_odd_flag:
            odd_number_collection.append(candidate)
    odd_number_collection.sort()
    return odd_number_collection