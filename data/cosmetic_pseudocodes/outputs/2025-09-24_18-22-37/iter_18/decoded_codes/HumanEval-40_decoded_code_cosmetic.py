from typing import Sequence

def triples_sum_to_zero(array_of_numbers: Sequence[int]) -> bool:
    n = len(array_of_numbers)
    position_a = 0
    while position_a <= n - 1:
        position_b = position_a + 1
        while True:
            if position_b > n - 1:
                break
            position_c = position_b + 1
            while True:
                if position_c > n - 1:
                    break
                partial_sum = array_of_numbers[position_a] + array_of_numbers[position_b] + array_of_numbers[position_c]
                if partial_sum == 0:
                    return True
                position_c += 1
            position_b += 1
        position_a += 1
    return False