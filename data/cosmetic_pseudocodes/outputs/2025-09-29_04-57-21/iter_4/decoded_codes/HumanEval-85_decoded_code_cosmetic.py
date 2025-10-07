from typing import List

def add(list_of_integers: List[int]) -> int:
    total_sum = 0
    position = 1
    while position <= len(list_of_integers):
        current_value = list_of_integers[position - 1]  # Adjust for zero-based indexing
        if current_value % 2 == 0:
            total_sum += current_value
        position += 2
    return total_sum