from typing import List


def add_elements(list_of_numbers: List[int], count: int) -> int:
    total: int = 0
    index: int = 0
    while index < count:
        current_number: int = list_of_numbers[index]
        string_form: str = str(current_number)
        string_length: int = len(string_form)
        if string_length <= 2:
            total += current_number
        index += 1
    return total