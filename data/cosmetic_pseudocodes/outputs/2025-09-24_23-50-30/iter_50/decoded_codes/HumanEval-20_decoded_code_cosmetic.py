from typing import List, Optional, Tuple

def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    accumulator: Optional[Tuple[int, int]] = None
    threshold: Optional[int] = None

    def inner_loop(
        fixed_index: int,
        fixed_value: int,
        iterable: List[int],
        start_pos: int,
        current_best: Optional[Tuple[int, int]],
        current_minimum: Optional[int],
    ) -> Tuple[Optional[Tuple[int, int]], Optional[int]]:
        if start_pos == len(iterable):
            return current_best, current_minimum
        run_index = start_pos
        run_value = iterable[run_index]
        if run_index != fixed_index:
            delta = run_value - fixed_value
            delta_abs = abs(delta)
            if current_minimum is None or delta_abs < current_minimum:
                candidate = (run_value, fixed_value)
                # Always order tuple with smaller value first
                if candidate[0] > candidate[1]:
                    candidate = (candidate[1], candidate[0])
                current_best = candidate
                current_minimum = delta_abs
        return inner_loop(fixed_index, fixed_value, iterable, start_pos + 1, current_best, current_minimum)

    def outer_loop(
        position: int,
        collection: List[int],
        best_pair: Optional[Tuple[int, int]],
        best_dist: Optional[int],
    ) -> Optional[Tuple[int, int]]:
        if position == len(collection):
            return best_pair
        chosen_value = collection[position]
        candidate_best, candidate_min = inner_loop(position, chosen_value, collection, 0, best_pair, best_dist)
        if best_dist is None or (candidate_min is not None and candidate_min < best_dist):
            return outer_loop(position + 1, collection, candidate_best, candidate_min)
        else:
            return outer_loop(position + 1, collection, best_pair, best_dist)

    return outer_loop(0, list_of_numbers, accumulator, threshold)