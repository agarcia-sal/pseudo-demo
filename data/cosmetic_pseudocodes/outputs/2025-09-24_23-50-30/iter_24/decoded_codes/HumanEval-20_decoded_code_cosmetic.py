from typing import List, Optional, Tuple


def find_closest_elements(array_of_vals: List[int]) -> Optional[Tuple[int, int]]:
    pair_result: Optional[Tuple[int, int]] = None
    dist_minimum: Optional[int] = None

    length = len(array_of_vals)
    for i_outer in range(length):
        for j_inner in range(length):
            if i_outer != j_inner:
                diff = array_of_vals[j_inner] - array_of_vals[i_outer]
                dist = abs(diff)  # absolute difference represents the 'distance'

                if dist_minimum is None or dist < dist_minimum:
                    dist_minimum = dist
                    if array_of_vals[i_outer] < array_of_vals[j_inner]:
                        pair_result = (array_of_vals[i_outer], array_of_vals[j_inner])
                    else:
                        pair_result = (array_of_vals[j_inner], array_of_vals[i_outer])

    return pair_result