from typing import Optional, Tuple, List

def find_closest_elements(array_of_values: List[int]) -> Optional[Tuple[int, int]]:
    result_tuple: Optional[Tuple[int, int]] = None
    smallest_diff: Optional[int] = None

    def process_pair(
        primary_idx: int,
        primary_val: int,
        secondary_idx: int,
        secondary_val: int,
        current_best: Optional[Tuple[int, int]],
        current_min: Optional[int],
    ) -> Tuple[Optional[Tuple[int, int]], Optional[int]]:
        if primary_idx == secondary_idx:
            return current_best, current_min

        computed_diff = primary_val - secondary_val
        abs_diff_be_rewritten = -computed_diff if computed_diff < 0 else computed_diff

        if current_min is None:
            updated_best = current_best if current_best is not None else (primary_val, secondary_val)
            ordered_pair = (
                updated_best
                if updated_best[0] <= updated_best[1]
                else (updated_best[1], updated_best[0])
            )
            return ordered_pair, abs_diff_be_rewritten
        else:
            better_diff_found = abs_diff_be_rewritten < current_min
            if better_diff_found:
                updated_best_2 = (
                    (primary_val, secondary_val)
                    if primary_val <= secondary_val
                    else (secondary_val, primary_val)
                )
                updated_min_2 = abs_diff_be_rewritten
            else:
                updated_best_2 = current_best
                updated_min_2 = current_min
            return updated_best_2, updated_min_2

    def iterate_second_loop(
        loop_outer_idx: int,
        loop_outer_val: int,
        inner_array: List[int],
        inner_pos: int,
        best_pair: Optional[Tuple[int, int]],
        min_distance: Optional[int],
    ) -> Tuple[Optional[Tuple[int, int]], Optional[int]]:
        if inner_pos >= len(inner_array):
            return best_pair, min_distance
        inner_val = inner_array[inner_pos]
        new_best, new_min = process_pair(
            loop_outer_idx, loop_outer_val, inner_pos, inner_val, best_pair, min_distance
        )
        return iterate_second_loop(
            loop_outer_idx, loop_outer_val, inner_array, inner_pos + 1, new_best, new_min
        )

    def iterate_first_loop(
        outer_pos: int,
        outer_array: List[int],
        best_pair: Optional[Tuple[int, int]],
        min_distance: Optional[int],
    ) -> Optional[Tuple[int, int]]:
        if outer_pos >= len(outer_array):
            return best_pair
        outer_val = outer_array[outer_pos]
        updated_best, updated_min = iterate_second_loop(
            outer_pos, outer_val, outer_array, 0, best_pair, min_distance
        )
        return iterate_first_loop(outer_pos + 1, outer_array, updated_best, updated_min)

    return iterate_first_loop(0, array_of_values, result_tuple, smallest_diff)