from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    length = len(list_of_integers)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if list_of_integers[i] + list_of_integers[j] + list_of_integers[k] == 0:
                    return True
    return False