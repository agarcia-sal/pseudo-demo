from typing import Callable

def hex_key(string_num: str) -> int:
    def count_accumulator(acc: int, curr: str) -> int:
        # Increment acc if curr is one of the specified characters
        if curr in {'2', '3', '5', '7', 'B', 'D'}:
            return acc + 1
        return acc

    def recurse_count(seq: str, pos: int, acc: int) -> int:
        # Base case: reached end of sequence
        if pos >= len(seq):
            return acc
        # Recurse with next position and updated accumulator
        return recurse_count(seq, pos + 1, count_accumulator(acc, seq[pos]))

    return recurse_count(string_num, 0, 0)