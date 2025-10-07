from typing import List, TypeVar

T = TypeVar('T')

def sort_third(input_list: List[T]) -> List[T]:
    working_list = input_list.copy()
    indices_divisible_by_three = [i for i in range(len(working_list)) if i % 3 == 0]
    elements_at_indices_divisible_by_three = [working_list[i] for i in indices_divisible_by_three]
    sorted_elements = sorted(elements_at_indices_divisible_by_three)
    for idx, val in zip(indices_divisible_by_three, sorted_elements):
        working_list[idx] = val
    return working_list