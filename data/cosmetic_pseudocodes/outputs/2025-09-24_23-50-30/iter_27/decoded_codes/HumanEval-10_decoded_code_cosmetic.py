from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def is_palindrome(data_sequence: T) -> bool:
    return data_sequence == data_sequence[::-1]

def make_palindrome(sequence_input: str) -> str:
    if sequence_input == "":
        return ""

    idx_suffix_start = 0

    # Find the smallest suffix start index to make the substring a palindrome
    while not is_palindrome(sequence_input[idx_suffix_start:]):
        idx_suffix_start += 1

    return sequence_input + sequence_input[:idx_suffix_start][::-1]