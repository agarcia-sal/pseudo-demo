from typing import Sequence


def triples_sum_to_zero(sequence: Sequence[int]) -> bool:
    def helper_outer(counter: int) -> bool:
        if counter == len(sequence):
            return False
        return helper_middle(counter, counter + 1)

    def helper_middle(first: int, second: int) -> bool:
        if second == len(sequence):
            return helper_outer(first + 1)
        return helper_inner(first, second, second + 1)

    def helper_inner(a: int, b: int, c: int) -> bool:
        if c == len(sequence):
            return helper_middle(a, b + 1)
        if sequence[a] + sequence[b] + sequence[c] == 0:
            return True
        return helper_inner(a, b, c + 1)

    return helper_outer(0)