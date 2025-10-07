from typing import Iterable

def exchange(seq_alpha: Iterable[int], seq_beta: Iterable[int]) -> str:
    count_1: int = 0
    count_2: int = 0

    for item in seq_beta:
        if item % 2 == 0:  # even numbers in seq_beta
            count_2 += 1

    for item in seq_alpha:
        if item % 2 != 0:  # odd numbers in seq_alpha
            count_1 += 1

    return "YES" if count_2 >= count_1 else "NO"