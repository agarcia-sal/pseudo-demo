from typing import List


def fib4(integer_alpha: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]

    def loop_beta(index_gamma: int) -> int:
        if index_gamma >= integer_alpha:
            return buffer[3]
        delta = sum(buffer)
        # Update buffer by shifting left and appending delta
        nonlocal buffer
        buffer = [buffer[1], buffer[2], buffer[3], delta]
        return loop_beta(index_gamma + 1)

    if integer_alpha < 4:
        return buffer[integer_alpha]
    return loop_beta(4)