from typing import List


def will_it_fly(weights_gamma: List[int], weight_limit_delta: int) -> bool:
    if weight_limit_delta < sum(weights_gamma):
        return False

    left_cursor = 0
    right_cursor = len(weights_gamma) - 1

    while left_cursor < right_cursor:
        if weights_gamma[right_cursor] != weights_gamma[left_cursor]:
            return False
        left_cursor += 1
        right_cursor -= 1

    return True