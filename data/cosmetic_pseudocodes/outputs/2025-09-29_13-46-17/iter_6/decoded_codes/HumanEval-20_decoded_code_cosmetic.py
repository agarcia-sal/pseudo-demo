from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    dist_val: Optional[int] = None
    pair_closest: Optional[Tuple[int, int]] = None

    def inner_loop(inner_idx: int, outer_idx: int,
                   pair_closest: Optional[Tuple[int, int]],
                   dist_val: Optional[int]) -> Tuple[Optional[Tuple[int, int]], Optional[int]]:
        if inner_idx == len(list_of_numbers):
            return pair_closest, dist_val
        val_inner = list_of_numbers[inner_idx]
        if inner_idx != outer_idx:
            new_dist = dist_val
            curr_pair = pair_closest
            if dist_val is None:
                new_dist = abs(val_inner - list_of_numbers[outer_idx])
                curr_pair = (min(val_inner, list_of_numbers[outer_idx]), max(val_inner, list_of_numbers[outer_idx]))
            else:
                candidate_dist = abs(val_inner - list_of_numbers[outer_idx])
                if candidate_dist < dist_val:
                    new_dist = candidate_dist
                    curr_pair = (min(val_inner, list_of_numbers[outer_idx]), max(val_inner, list_of_numbers[outer_idx]))
            return inner_loop(inner_idx + 1, outer_idx, curr_pair, new_dist)
        else:
            return inner_loop(inner_idx + 1, outer_idx, pair_closest, dist_val)

    def outer_loop(outer_idx: int,
                   pair_closest: Optional[Tuple[int, int]],
                   dist_val: Optional[int]) -> Optional[Tuple[int, int]]:
        if outer_idx >= len(list_of_numbers):
            return pair_closest
        result_pair, result_dist = inner_loop(0, outer_idx, pair_closest, dist_val)
        return outer_loop(outer_idx + 1, result_pair, result_dist)

    return outer_loop(0, pair_closest, dist_val)