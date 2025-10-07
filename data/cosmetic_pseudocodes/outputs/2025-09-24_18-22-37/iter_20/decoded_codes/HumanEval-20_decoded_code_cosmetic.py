from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    best_pair: Optional[Tuple[int, int]] = None
    smallest_diff: Optional[int] = None
    i = 0

    while i < len(list_of_numbers):
        val_i = list_of_numbers[i]
        j = 0
        while j < len(list_of_numbers):
            val_j = list_of_numbers[j]
            if i != j:
                temp_diff = val_i - val_j
                current_diff = -temp_diff if temp_diff < 0 else temp_diff

                if smallest_diff is None or current_diff < smallest_diff:
                    smallest_diff = current_diff
                    temp_tuple = (val_i, val_j)
                    if temp_tuple[0] > temp_tuple[1]:
                        best_pair = (temp_tuple[1], temp_tuple[0])
                    else:
                        best_pair = temp_tuple
            j += 1
        i += 1

    return best_pair