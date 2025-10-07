from typing import Sequence


def triples_sum_to_zero(numbers_array: Sequence[int]) -> bool:
    length_var: int = len(numbers_array)
    pos1: int = 0
    while pos1 < length_var - 2:
        pos2: int = pos1 + 1
        while pos2 < length_var - 1:
            pos3: int = pos2 + 1
            while pos3 < length_var:
                if not (numbers_array[pos1] + numbers_array[pos2] + numbers_array[pos3] != 0):
                    return True
                pos3 += 1
            pos2 += 1
        pos1 += 1
    return False