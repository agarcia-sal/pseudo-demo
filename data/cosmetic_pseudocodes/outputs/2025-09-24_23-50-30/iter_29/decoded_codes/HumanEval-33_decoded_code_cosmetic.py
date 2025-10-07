from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    temp_list: List[T] = list_input[:]
    divisible_indices_values: List[T] = [temp_list[i] for i in range(len(temp_list)) if i % 3 == 0]
    ordered_values: List[T] = sorted(divisible_indices_values)
    idx = 0
    for index in range(len(temp_list)):
        if index % 3 == 0:
            temp_list[index] = ordered_values[idx]
            idx += 1
    return temp_list