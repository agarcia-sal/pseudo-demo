from typing import Iterable, List


def unique_digits(numbers_collection: Iterable[int]) -> List[int]:
    filtered_numbers: List[int] = []
    index_counter: int = 0
    numbers_list = list(numbers_collection)  # Ensure indexing support
    while index_counter < len(numbers_list):
        current_number = numbers_list[index_counter]
        is_all_digits_odd = True
        temp_number = current_number
        while temp_number > 0 and is_all_digits_odd:
            digit_value = temp_number % 10
            if digit_value % 2 == 0:
                is_all_digits_odd = False
            temp_number //= 10
        if is_all_digits_odd:
            filtered_numbers.append(current_number)
        index_counter += 1
    return sorted(filtered_numbers)