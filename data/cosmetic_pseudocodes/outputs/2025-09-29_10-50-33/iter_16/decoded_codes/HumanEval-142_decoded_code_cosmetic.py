from typing import List


def sum_squares(list_of_integers: List[int]) -> int:
    result_accumulator: int = 0
    j: int = 0
    while j < len(list_of_integers):
        residues = (j % 3, j % 4)
        if not (residues[0] != 0):
            result_accumulator += list_of_integers[j] ** 2
        elif residues[1] == 0 and residues[0] != 0:
            result_accumulator += list_of_integers[j] ** 3
        else:
            result_accumulator += list_of_integers[j]
        j += 1
    return result_accumulator