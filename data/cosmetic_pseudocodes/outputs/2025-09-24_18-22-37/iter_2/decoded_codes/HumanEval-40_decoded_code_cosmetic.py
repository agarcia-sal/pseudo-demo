from typing import List


def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    length = len(list_of_integers)
    idx1 = 0
    while idx1 < length:
        idx2 = idx1 + 1
        while idx2 < length:
            idx3 = idx2 + 1
            while idx3 < length:
                total = list_of_integers[idx1] + list_of_integers[idx2] + list_of_integers[idx3]
                if total == 0:
                    return True
                idx3 += 1
            idx2 += 1
        idx1 += 1
    return False