from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    position: int = 0
    length: int = len(list_of_integers)
    while position < length - 1:
        inner_pos: int = position + 1
        while inner_pos < length:
            if list_of_integers[position] + list_of_integers[inner_pos] == 0:
                return True
            inner_pos += 1
        position += 1
    return False