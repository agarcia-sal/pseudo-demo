from typing import List


def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    outer_index = 0
    length = len(list_of_integers)
    while outer_index < length:
        middle_index = outer_index + 1
        while middle_index < length:
            inner_index = middle_index + 1
            while inner_index < length:
                sum_value = (
                    list_of_integers[outer_index]
                    + list_of_integers[middle_index]
                    + list_of_integers[inner_index]
                )
                if sum_value == 0:
                    return True
                inner_index += 1
            middle_index += 1
        outer_index += 1
    return False