from typing import List

def get_positive(list_of_numbers: List[int]) -> List[int]:
    return [num for num in list_of_numbers if num > 0]