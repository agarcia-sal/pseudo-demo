from typing import List, Tuple


def is_nested(input_string: str) -> bool:
    def fold_indices(accumulator_opp: List[int], accumulator_clp: List[int], cursor: int) -> Tuple[List[int], List[int]]:
        if cursor >= len(input_string):
            return accumulator_opp, accumulator_clp
        if input_string[cursor] == '[':
            return fold_indices(accumulator_opp + [cursor], accumulator_clp, cursor + 1)
        else:
            return fold_indices(accumulator_opp, accumulator_clp + [cursor], cursor + 1)

    openings, closings = fold_indices([], [], 0)

    def reverse_list(orig_list: List[int], rev_list: List[int]) -> List[int]:
        if not orig_list:
            return rev_list
        return reverse_list(orig_list[1:], [orig_list[0]] + rev_list)

    reversed_closings = reverse_list(closings, [])

    def walk_lists(idx_open: int, idx_close: int, match_count: int) -> int:
        if idx_open >= len(openings) or idx_close >= len(reversed_closings):
            return match_count
        if openings[idx_open] < reversed_closings[idx_close]:
            return walk_lists(idx_open + 1, idx_close + 1, match_count + 1)
        else:
            return walk_lists(idx_open + 1, idx_close, match_count)

    matched_count = walk_lists(0, 0, 0)
    return matched_count >= 2