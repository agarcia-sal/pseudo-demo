from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    size: int = len(list_of_integers)
    i: int = 0
    while i < size - 2:
        j: int = i + 1
        while j < size - 1:
            k: int = j + 1
            while k < size:
                total: int = list_of_integers[i] + list_of_integers[j] + list_of_integers[k]
                if total == 0:
                    return True
                k += 1
            j += 1
        i += 1
    return False