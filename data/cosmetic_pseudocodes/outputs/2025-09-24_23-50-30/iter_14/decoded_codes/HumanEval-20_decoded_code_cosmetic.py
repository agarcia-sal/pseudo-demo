from typing import List, Optional, Tuple

def find_closest_elements(numbers: List[int]) -> Optional[Tuple[int, int]]:
    def iterate_outer(i: int, best_pair: Optional[Tuple[int, int]], best_diff: Optional[int]) -> Optional[Tuple[int, int]]:
        if i >= len(numbers):
            return best_pair

        def iterate_inner(j: int, current_best_pair: Optional[Tuple[int, int]], current_best_diff: Optional[int]) -> Tuple[Optional[Tuple[int, int]], Optional[int]]:
            if j >= len(numbers):
                return current_best_pair, current_best_diff

            if i == j:
                return iterate_inner(j + 1, current_best_pair, current_best_diff)

            diff = numbers[i] - numbers[j]
            dist = diff if diff >= 0 else -diff

            if current_best_diff is None or dist < current_best_diff:
                pair = (numbers[i], numbers[j]) if numbers[i] <= numbers[j] else (numbers[j], numbers[i])
                return iterate_inner(j + 1, pair, dist)
            else:
                return iterate_inner(j + 1, current_best_pair, current_best_diff)

        updated_pair, updated_diff = iterate_inner(0, best_pair, best_diff)
        return iterate_outer(i + 1, updated_pair, updated_diff)

    return iterate_outer(0, None, None)