from typing import Callable


def how_many_times(input_alpha: str, input_beta: str) -> int:
    def count_occur(pos: int, acc: int) -> int:
        if pos > len(input_alpha) - len(input_beta):
            return acc
        if input_alpha[pos : pos + len(input_beta)] == input_beta:
            return count_occur(pos + 1, acc + 1)
        return count_occur(pos + 1, acc)

    return count_occur(0, 0)