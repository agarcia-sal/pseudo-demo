from typing import Sequence, List, TypeVar

T = TypeVar('T')


def sort_third(container_param: Sequence[T]) -> List[T]:
    duplicate_list: List[T] = list(container_param)
    divisible_three_values: List[T] = []

    # Collect elements at indices divisible by 3
    current_idx = 0
    while current_idx < len(duplicate_list):
        if current_idx % 3 == 0:
            divisible_three_values.append(duplicate_list[current_idx])
        current_idx += 1

    ordered_subset: List[T] = []
    flag_done = False

    # Selection-sort-like manual sort of divisible_three_values into ordered_subset
    while not flag_done:
        if not divisible_three_values:
            flag_done = True
        else:
            smallest_value = divisible_three_values[0]
            position_tracker = 0
            current_idx = 1
            while current_idx < len(divisible_three_values):
                if divisible_three_values[current_idx] < smallest_value:
                    smallest_value = divisible_three_values[current_idx]
                    position_tracker = current_idx
                current_idx += 1
            ordered_subset.append(smallest_value)
            divisible_three_values.pop(position_tracker)

    # Replace elements at indices divisible by 3 in duplicate_list with sorted values
    position_tracker = 0
    current_idx = 0
    while current_idx < len(duplicate_list):
        if current_idx % 3 == 0:
            duplicate_list[current_idx] = ordered_subset[position_tracker]
            position_tracker += 1
        current_idx += 1

    return duplicate_list