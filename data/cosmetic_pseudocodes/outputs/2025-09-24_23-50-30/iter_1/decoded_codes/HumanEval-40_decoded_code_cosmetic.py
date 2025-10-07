from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n: int = len(list_of_integers)
    found: bool = False
    i: int = 0

    while i < n - 2 and not found:
        j: int = i + 1
        while j < n - 1 and not found:
            k: int = j + 1
            while k < n and not found:
                if list_of_integers[i] + list_of_integers[j] + list_of_integers[k] == 0:
                    found = True
                else:
                    k += 1
            j += 1
        i += 1

    return found