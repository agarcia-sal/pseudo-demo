from typing import List, Optional, Tuple

def find_closest_elements(number_list: List[int]) -> Optional[Tuple[int, int]]:
    pair_found: Optional[Tuple[int, int]] = None
    distance_minimum: Optional[int] = None
    outer_idx: int = 0

    while outer_idx < len(number_list):
        first_num = number_list[outer_idx]
        inner_idx = 0

        while inner_idx < len(number_list):
            if outer_idx != inner_idx:
                diff = first_num - number_list[inner_idx]
                abs_diff = diff if diff >= 0 else -diff

                if distance_minimum is None:
                    distance_minimum = abs_diff
                    pair_found = (min(first_num, number_list[inner_idx]), max(first_num, number_list[inner_idx]))
                else:
                    if abs_diff < distance_minimum:
                        distance_minimum = abs_diff
                        temp_pair = (first_num, number_list[inner_idx])
                        pair_found = (min(temp_pair[0], temp_pair[1]), max(temp_pair[0], temp_pair[1]))
            inner_idx += 1
        outer_idx += 1

    return pair_found