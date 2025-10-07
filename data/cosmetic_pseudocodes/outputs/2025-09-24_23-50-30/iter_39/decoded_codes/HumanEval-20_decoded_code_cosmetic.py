from typing import Optional, Tuple, List

def find_closest_elements(array_input: List[int]) -> Optional[Tuple[int, int]]:
    result_pair: Optional[Tuple[int, int]] = None
    smallest_diff: Optional[int] = None

    def iterate_pairs(i: int, j: int, res: Optional[Tuple[int, int]], diff: Optional[int]) -> Optional[Tuple[int, int]]:
        if i >= len(array_input):
            return res
        if j >= len(array_input):
            return iterate_pairs(i + 1, 0, res, diff)
        if i == j:
            return iterate_pairs(i, j + 1, res, diff)

        current_diff = abs(array_input[i] - array_input[j])

        if diff is None or current_diff < diff:
            pair = (array_input[i], array_input[j]) if array_input[i] < array_input[j] else (array_input[j], array_input[i])
            return iterate_pairs(i, j + 1, pair, current_diff)
        else:
            return iterate_pairs(i, j + 1, res, diff)

    return iterate_pairs(0, 0, result_pair, smallest_diff)