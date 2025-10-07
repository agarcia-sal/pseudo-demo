from typing import List

def minSubArraySum(array_of_ints: List[int]) -> int:
    accumulator: int = 0
    best_score: int = 0
    iterator_index: int = 0

    while iterator_index < len(array_of_ints):
        current_element: int = array_of_ints[iterator_index]
        delta: int = -current_element
        accumulator += delta
        if accumulator < 0:
            accumulator = 0
        if best_score < accumulator:
            best_score = accumulator
        iterator_index += 1

    if best_score == 0:
        temp_list: List[int] = []
        pos: int = 0
        while pos < len(array_of_ints):
            val: int = array_of_ints[pos]
            negated_val: int = -val
            temp_list.append(negated_val)
            pos += 1
        best_score = temp_list[0]
        idx: int = 1
        while idx < len(temp_list):
            if best_score < temp_list[idx]:
                best_score = temp_list[idx]
            idx += 1

    result_value: int = -best_score
    return result_value