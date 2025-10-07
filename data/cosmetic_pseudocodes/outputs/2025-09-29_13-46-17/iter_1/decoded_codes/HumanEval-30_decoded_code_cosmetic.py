from typing import List

def get_positive(list_of_numbers: List[int]) -> List[int]:
    return [element for element in list_of_numbers if element > 0]