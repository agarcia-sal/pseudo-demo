from typing import List

def max_element(list_of_numbers: List[int]) -> int:
    if not list_of_numbers:
        raise ValueError("list_of_numbers must not be empty")
    max_value: int = list_of_numbers[0]
    for element in list_of_numbers:
        if element > max_value:
            max_value = element
    return max_value