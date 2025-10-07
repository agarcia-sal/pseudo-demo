from typing import List


def fib4(integer_alpha: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]

    if integer_alpha < 4:
        return buffer[integer_alpha]

    def recur_beta(integer_gamma: int, sequence_delta: List[int]) -> int:
        if integer_gamma > integer_alpha:
            return sequence_delta[-1]
        accumulated_eta = sum(sequence_delta[-4:])
        truncated_theta = sequence_delta[1:] + [accumulated_eta]
        return recur_beta(integer_gamma + 1, truncated_theta)

    return recur_beta(4, buffer)