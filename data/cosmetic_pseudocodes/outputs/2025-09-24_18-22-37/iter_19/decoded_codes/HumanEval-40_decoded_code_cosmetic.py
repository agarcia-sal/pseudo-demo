from typing import Sequence

def triples_sum_to_zero(input_sequence: Sequence[int]) -> bool:
    length = len(input_sequence)
    outer_idx = 0
    while outer_idx <= length - 1:
        mid_idx = outer_idx + 1
        while True:
            if mid_idx > length - 1:
                break
            inner_idx = mid_idx + 1
            while True:
                if inner_idx > length - 1:
                    break
                first_element = input_sequence[outer_idx]
                second_element = input_sequence[mid_idx]
                third_element = input_sequence[inner_idx]
                summation = first_element + second_element + third_element
                if summation == 0:
                    return True
                inner_idx += 1
            mid_idx += 1
        outer_idx += 1
    return False