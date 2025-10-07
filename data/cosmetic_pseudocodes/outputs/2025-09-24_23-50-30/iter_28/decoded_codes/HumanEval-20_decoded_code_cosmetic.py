from typing import Sequence, Optional, Tuple


def find_closest_elements(input_sequence: Sequence[int]) -> Optional[Tuple[int, int]]:
    result_pair: Optional[Tuple[int, int]] = None
    best_diff: Optional[int] = None

    def loop_outer(pos_outer: int) -> None:
        if pos_outer >= len(input_sequence):
            return

        def loop_inner(pos_inner: int) -> None:
            nonlocal best_diff, result_pair
            if pos_inner >= len(input_sequence):
                return
            if pos_outer != pos_inner:
                curr_diff = abs(input_sequence[pos_outer] - input_sequence[pos_inner])
                if best_diff is None or curr_diff < best_diff:
                    best_diff = curr_diff
                    low, high = sorted((input_sequence[pos_outer], input_sequence[pos_inner]))
                    result_pair = (low, high)
            loop_inner(pos_inner + 1)

        loop_inner(0)
        loop_outer(pos_outer + 1)

    loop_outer(0)
    return result_pair