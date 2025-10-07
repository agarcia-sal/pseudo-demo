from typing import Sequence


def solution(sequence_of_numbers: Sequence[int]) -> int:
    acc: int = 0
    pos: int = 0
    while pos < len(sequence_of_numbers):
        if pos % 2 == 0:
            if sequence_of_numbers[pos] % 2 == 1:
                acc += sequence_of_numbers[pos]
        pos += 1
    return acc