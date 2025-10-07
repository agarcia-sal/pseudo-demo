from typing import List, Optional, Tuple

def find_closest_elements(array_of_values: List[int]) -> Optional[Tuple[int, int]]:
    candidate_pair: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    i: int = 0
    while True:
        if i >= len(array_of_values):
            break

        j: int = 0
        while True:
            if j >= len(array_of_values):
                break

            first_elem: int = array_of_values[i]
            second_elem: int = array_of_values[j]

            if i != j:
                diff: int = first_elem - second_elem
                ABS_diff: int = diff if diff >= 0 else -diff

                if smallest_gap is None:
                    # Initialize candidate_pair in sorted order
                    candidate_pair = (first_elem, second_elem)
                    if candidate_pair[0] > candidate_pair[1]:
                        candidate_pair = (candidate_pair[1], candidate_pair[0])
                    smallest_gap = ABS_diff
                elif ABS_diff < smallest_gap:
                    tmp_pair = (first_elem, second_elem)
                    if tmp_pair[0] > tmp_pair[1]:
                        tmp_pair = (tmp_pair[1], tmp_pair[0])
                    candidate_pair = tmp_pair
                    smallest_gap = ABS_diff

            j += 1
        i += 1

    return candidate_pair