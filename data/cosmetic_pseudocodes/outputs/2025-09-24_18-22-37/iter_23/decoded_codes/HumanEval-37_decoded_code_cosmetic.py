from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_even(sequence: Sequence[T]) -> List[T]:
    temp_even: List[T] = []
    temp_odd: List[T] = []

    counter_a = 0
    counter_b = 1
    length = len(sequence)

    while counter_a < length:
        temp_even.append(sequence[counter_a])
        counter_a += 2

    while counter_b < length:
        temp_odd.append(sequence[counter_b])
        counter_b += 2

    temp_even.sort()  # Sort evens non-decreasing

    final_result: List[T] = []
    idx_even = 0
    idx_odd = 0

    while True:
        if idx_even >= len(temp_even) or idx_odd >= len(temp_odd):
            break
        element_pair = [temp_even[idx_even], temp_odd[idx_odd]]
        final_result.extend(element_pair)
        idx_even += 1
        idx_odd += 1

    if len(temp_even) > len(temp_odd):
        extra_element = temp_even[-1]
        final_result.append(extra_element)

    return final_result