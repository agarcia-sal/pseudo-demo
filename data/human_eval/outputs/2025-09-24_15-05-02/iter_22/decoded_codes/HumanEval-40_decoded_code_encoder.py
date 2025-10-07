from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n = len(list_of_integers)
    for first_index in range(n):
        for second_index in range(first_index + 1, n):
            for third_index in range(second_index + 1, n):
                if list_of_integers[first_index] + list_of_integers[second_index] + list_of_integers[third_index] == 0:
                    return True
    return False