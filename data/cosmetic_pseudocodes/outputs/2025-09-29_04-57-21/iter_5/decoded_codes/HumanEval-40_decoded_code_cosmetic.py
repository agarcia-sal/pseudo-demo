from typing import List

def triples_sum_to_zero(input_array: List[int]) -> bool:
    n = len(input_array)
    for first_pointer in range(n - 2):
        for second_pointer in range(first_pointer + 1, n - 1):
            for third_pointer in range(second_pointer + 1, n):
                if input_array[first_pointer] + input_array[second_pointer] + input_array[third_pointer] == 0:
                    return True
    return False