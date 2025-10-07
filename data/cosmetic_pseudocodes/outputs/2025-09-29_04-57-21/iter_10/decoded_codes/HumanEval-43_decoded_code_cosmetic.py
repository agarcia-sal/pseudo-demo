from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    current_position: int = 0
    length: int = len(list_of_integers)
    while current_position < length - 1:
        secondary_position: int = current_position + 1
        while secondary_position < length:
            if list_of_integers[secondary_position] + list_of_integers[current_position] == 0:
                return True
            secondary_position += 1
        current_position += 1
    return False