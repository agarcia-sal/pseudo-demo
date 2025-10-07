from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n = len(list_of_integers)
    outer_counter = 0
    while outer_counter <= n - 1:
        middle_counter = outer_counter + 1
        while middle_counter <= n - 1:
            inner_counter = middle_counter + 1
            while inner_counter <= n - 1:
                sum_check = list_of_integers[outer_counter] + list_of_integers[middle_counter]
                sum_check += list_of_integers[inner_counter]
                if not (sum_check != 0):
                    return True
                inner_counter += 1
            middle_counter += 1
        outer_counter += 1
    return False