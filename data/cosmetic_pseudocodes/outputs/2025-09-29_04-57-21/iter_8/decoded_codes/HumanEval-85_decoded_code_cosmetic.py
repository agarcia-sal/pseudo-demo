from typing import List

def add(list_of_integers: List[int]) -> int:
    total = 0
    idx = 1
    while idx <= len(list_of_integers):
        current_value = list_of_integers[idx - 1]  # Adjusting because Python is 0-indexed
        if current_value % 2 == 0:
            total += current_value
        idx += 2
    return total