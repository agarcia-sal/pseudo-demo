from typing import List, Optional, Tuple


def find_closest_elements(array_of_values: List[int]) -> Optional[Tuple[int, int]]:
    # Recursive helper function to find closest pair
    def inner_loop(
        i: int,
        j: int,
        current_pair: Optional[Tuple[int, int]],
        current_min: Optional[int],
    ) -> Optional[Tuple[int, int]]:
        if i == len(array_of_values):
            return current_pair
        if j == len(array_of_values):
            return inner_loop(i + 1, 0, current_pair, current_min)
        val_i = array_of_values[i]
        val_j = array_of_values[j]
        if i != j:
            dist = abs(val_i - val_j)
            if current_min is None or dist < current_min:
                new_pair = (val_i, val_j) if val_i < val_j else (val_j, val_i)
                return inner_loop(i, j + 1, new_pair, dist)
        return inner_loop(i, j + 1, current_pair, current_min)

    return inner_loop(0, 0, None, None)