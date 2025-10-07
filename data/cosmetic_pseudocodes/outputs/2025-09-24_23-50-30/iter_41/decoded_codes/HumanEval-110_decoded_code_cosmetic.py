from typing import Sequence

def exchange(sequence_alpha: Sequence[int], sequence_beta: Sequence[int]) -> str:
    def count_odd_recursive(seq: Sequence[int], idx: int, counter: int) -> int:
        if idx >= len(seq):
            return counter
        return count_odd_recursive(seq, idx + 1, counter + (seq[idx] % 2))

    def count_even_recursive(seq: Sequence[int], idx: int, counter: int) -> int:
        if idx >= len(seq):
            return counter
        return count_even_recursive(seq, idx + 1, counter + (1 - (seq[idx] % 2)))

    tally_1 = count_odd_recursive(sequence_alpha, 0, 0)
    tally_2 = count_even_recursive(sequence_beta, 0, 0)

    if tally_2 >= tally_1:
        return "YES"
    return "NO"