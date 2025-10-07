from typing import List

def triples_sum_to_zero(array_elements: List[int]) -> bool:
    n = len(array_elements)
    position_a = 0
    while position_a <= n - 1:
        position_b = position_a + 1
        while position_b <= n - 1:
            position_c = position_b + 1
            while position_c <= n - 1:
                if array_elements[position_a] + array_elements[position_b] + array_elements[position_c] == 0:
                    return True
                position_c += 1
            position_b += 1
        position_a += 1
    return False