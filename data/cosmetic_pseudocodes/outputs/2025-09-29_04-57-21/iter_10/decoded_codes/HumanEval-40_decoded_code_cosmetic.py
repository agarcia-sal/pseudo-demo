from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    outer_counter: int = 0
    n: int = len(list_of_integers)
    while outer_counter < n:
        middle_counter: int = outer_counter + 1
        while middle_counter < n:
            inner_counter: int = middle_counter + 1
            while inner_counter < n:
                if not (list_of_integers[outer_counter] + list_of_integers[middle_counter] + list_of_integers[inner_counter] != 0):
                    return True
                inner_counter += 1
            middle_counter += 1
        outer_counter += 1
    return False