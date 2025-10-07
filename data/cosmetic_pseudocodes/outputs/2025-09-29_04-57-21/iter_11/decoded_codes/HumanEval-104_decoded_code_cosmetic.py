from typing import Iterable, List


def unique_digits(numbers_collection: Iterable[int]) -> List[int]:
    filtered_numbers: List[int] = []
    index_counter: int = 0
    numbers_list = list(numbers_collection)  # to support indexing and length reliably
    while index_counter < len(numbers_list):
        current_value: int = numbers_list[index_counter]
        digit_cursor: int = 0
        all_are_odd: bool = True
        current_value_str = str(current_value)
        while digit_cursor < len(current_value_str):
            digit_char = current_value_str[digit_cursor]
            # Check if digit is not odd
            if (ord(digit_char) - ord('0')) % 2 != 1:
                all_are_odd = False
                break
            digit_cursor += 1
        index_counter += 1
        if all_are_odd:
            filtered_numbers = filtered_numbers + [current_value]
    return sorted(filtered_numbers)