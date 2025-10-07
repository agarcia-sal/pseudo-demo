from typing import List

def triples_sum_to_zero(array_elements: List[int]) -> bool:
    length = len(array_elements)
    for counter_a in range(length - 2):
        for counter_b in range(counter_a + 1, length - 1):
            for counter_c in range(counter_b + 1, length):
                if array_elements[counter_a] + array_elements[counter_b] + array_elements[counter_c] == 0:
                    return True
    return False