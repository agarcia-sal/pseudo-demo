from typing import List, Optional, Tuple


def find_closest_elements(numbers_array: List[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    distance_minimum: Optional[int] = None

    outer_index = 0
    length = len(numbers_array)

    while outer_index < length:
        outer_value = numbers_array[outer_index]
        inner_index = 0

        while inner_index < length:
            inner_value = numbers_array[inner_index]
            if outer_index == inner_index:
                inner_index += 1
                continue

            current_diff = abs(outer_value - inner_value)

            if distance_minimum is None:
                distance_minimum = current_diff
                pair_closest = (outer_value, inner_value)
                pair_closest = (
                    pair_closest if pair_closest[0] <= pair_closest[1]
                    else (pair_closest[1], pair_closest[0])
                )
            else:
                if current_diff < distance_minimum:
                    distance_minimum = current_diff
                    pair_closest = (outer_value, inner_value)
                    if pair_closest[0] > pair_closest[1]:
                        pair_closest = (pair_closest[1], pair_closest[0])

            inner_index += 1
        outer_index += 1

    return pair_closest