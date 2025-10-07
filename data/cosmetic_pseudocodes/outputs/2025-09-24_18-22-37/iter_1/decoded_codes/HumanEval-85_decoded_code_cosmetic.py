from typing import List


def add(list_of_integers: List[int]) -> int:
    total: int = 0
    index: int = 1
    while index <= len(list_of_integers):
        current_value: int = list_of_integers[index - 1]  # adjusting for 0-based indexing
        if current_value % 2 == 0:
            total += current_value
        index += 2
    return total