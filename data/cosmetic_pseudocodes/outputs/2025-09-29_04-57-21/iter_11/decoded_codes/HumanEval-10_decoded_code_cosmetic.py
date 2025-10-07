from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def is_palindrome(sequence: T) -> bool:
    return sequence == sequence[::-1]

def make_palindrome(sequence: str) -> str:
    if len(sequence) == 0:
        return ""
    index_start_suffix = 0
    while True:
        segment = sequence[index_start_suffix:]
        if is_palindrome(segment):
            break
        index_start_suffix += 1
    prefix_reversed = sequence[:index_start_suffix][::-1]
    return sequence + prefix_reversed