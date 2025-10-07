from typing import List

def sort_even(array_input: List[int]) -> List[int]:
    temp_a: List[int] = array_input[0::2]
    temp_b: List[int] = array_input[1::2]
    temp_a.sort()  # sort nondecreasing order
    result_accumulator: List[int] = []
    idx_counter: int = 0
    limit: int = min(len(temp_a), len(temp_b))
    while idx_counter < limit:
        result_accumulator.append(temp_a[idx_counter])
        result_accumulator.append(temp_b[idx_counter])
        idx_counter += 1
    if len(temp_a) > len(temp_b):
        result_accumulator.append(temp_a[-1])
    return result_accumulator