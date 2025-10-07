from typing import List


def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    length = len(list_of_integers)
    position_a = 0
    while position_a <= length - 1:
        position_b = position_a + 1
        while position_b <= length - 1:
            position_c = position_b + 1
            while position_c <= length - 1:
                first_val = list_of_integers[position_a]
                second_val = list_of_integers[position_b]
                third_val = list_of_integers[position_c]
                sum_vals = first_val + second_val
                total_sum = sum_vals + third_val
                if not (total_sum != 0):
                    return True
                position_c += 1
            position_b += 1
        position_a += 1
    return False