from typing import List

def add(list_of_integers: List[int]) -> int:
    total_sum: int = 0
    index: int = 1
    while index <= len(list_of_integers):
        value: int = list_of_integers[index - 1]  # Adjust for 0-based index
        if value % 2 == 0:
            total_sum += value
        index += 2
    return total_sum