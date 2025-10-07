from typing import Optional, Sequence, Tuple

def find_closest_elements(sequence_numbers: Sequence[int]) -> Optional[Tuple[int, int]]:
    pair_closest: Optional[Tuple[int, int]] = None
    dist_minimum: Optional[int] = None

    def aux_i(i: int, acc_pair: Optional[Tuple[int, int]], acc_dist: Optional[int]) -> Optional[Tuple[int, int]]:
        if i == len(sequence_numbers):
            return acc_pair
        return aux_j(i, 0, acc_pair, acc_dist, acc_pair, acc_dist)

    def aux_j(i: int, j: int,
              best_pair: Optional[Tuple[int, int]],
              best_dist: Optional[int],
              current_pair: Optional[Tuple[int, int]],
              current_dist: Optional[int]) -> Optional[Tuple[int, int]]:
        if j == len(sequence_numbers):
            return aux_i(i + 1, best_pair, best_dist)
        x = sequence_numbers[i]
        y = sequence_numbers[j]
        if i != j:
            dist_current = abs(x - y)
            if best_dist is None:
                sorted_pair = (x, y) if x < y else (y, x)
                best_dist = dist_current
                best_pair = sorted_pair
            elif dist_current < best_dist:
                sorted_pair = (x, y) if x < y else (y, x)
                best_dist = dist_current
                best_pair = sorted_pair
        return aux_j(i, j + 1, best_pair, best_dist, current_pair, current_dist)

    return aux_i(0, pair_closest, dist_minimum)