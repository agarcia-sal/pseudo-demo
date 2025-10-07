from typing import List

def triples_sum_to_zero(input_array: List[int]) -> bool:
    length: int = len(input_array)
    pointer_a: int = 0
    while pointer_a < length:
        pointer_b: int = pointer_a + 1
        while pointer_b < length:
            pointer_c: int = pointer_b + 1
            while pointer_c < length:
                sum_val: int = input_array[pointer_a] + input_array[pointer_b] + input_array[pointer_c]
                if sum_val == 0:
                    return True
                pointer_c += 1
            pointer_b += 1
        pointer_a += 1
    return False