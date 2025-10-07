from typing import List

def add(list_of_integers: List[int]) -> int:
    total: int = 0
    for index in range(1, len(list_of_integers), 2):
        current_element = list_of_integers[index]
        if current_element % 2 == 0:
            total += current_element
    return total