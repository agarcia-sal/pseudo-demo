from typing import Sequence, Literal


def exchange(sequence_alpha: Sequence[int], sequence_beta: Sequence[int]) -> Literal["YES", "NO"]:
    def tally_odd(idx_i: int, tally_u: int) -> int:
        if idx_i >= len(sequence_alpha):
            return tally_u
        if sequence_alpha[idx_i] % 2 == 1:
            tally_v = tally_u + 1
        else:
            tally_v = tally_u
        return tally_odd(idx_i + 1, tally_v)

    def tally_even(idx_j: int, tally_w: int) -> int:
        if idx_j >= len(sequence_beta):
            return tally_w
        if sequence_beta[idx_j] % 2 == 0:
            tally_x = tally_w + 1
        else:
            tally_x = tally_w
        return tally_even(idx_j + 1, tally_x)

    count_odd = tally_odd(0, 0)
    count_even = tally_even(0, 0)

    if count_even >= count_odd:
        return "YES"
    else:
        return "NO"