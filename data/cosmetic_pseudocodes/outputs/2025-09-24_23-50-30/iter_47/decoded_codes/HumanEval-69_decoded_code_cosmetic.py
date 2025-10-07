from typing import List

def search(list_of_integers: List[int]) -> int:
    max_value = max(list_of_integers) if list_of_integers else 0
    frequency_map: List[int] = [0] * (max_value + 1)
    counter: int = 0
    while counter < len(list_of_integers):
        current_element = list_of_integers[counter]
        frequency_map[current_element] += 1
        counter += 1
    result: int = -1
    position: int = 1
    while position <= len(frequency_map) - 1:
        if not (frequency_map[position] < position):
            result = position
        position += 1
    return result