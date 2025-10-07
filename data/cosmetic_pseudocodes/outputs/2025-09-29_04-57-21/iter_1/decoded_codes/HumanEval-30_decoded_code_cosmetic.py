from typing import List

def get_positive(numbers_array: List[int]) -> List[int]:
    positive_values: List[int] = [each_number for each_number in numbers_array if each_number > 0]
    return positive_values