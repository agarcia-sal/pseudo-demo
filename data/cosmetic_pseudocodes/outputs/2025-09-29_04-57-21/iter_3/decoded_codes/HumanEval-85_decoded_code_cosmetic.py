from typing import List

def add(list_of_integers: List[int]) -> int:
    accumulated_sum: int = 0
    for index in range(1, len(list_of_integers), 2):
        current_value: int = list_of_integers[index]
        if current_value % 2 == 0:
            accumulated_sum += current_value
    return accumulated_sum