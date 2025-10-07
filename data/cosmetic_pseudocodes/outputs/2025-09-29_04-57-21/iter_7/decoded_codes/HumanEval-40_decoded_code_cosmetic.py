from typing import List

def triples_sum_to_zero(input_array: List[int]) -> bool:
    n = len(input_array)
    outer_index = 0
    while outer_index <= n - 1:
        middle_index = outer_index + 1
        while middle_index <= n - 1:
            inner_index = middle_index + 1
            while inner_index <= n - 1:
                if not (input_array[outer_index] + input_array[middle_index] + input_array[inner_index] != 0):
                    return True
                inner_index += 1
            middle_index += 1
        outer_index += 1
    return False