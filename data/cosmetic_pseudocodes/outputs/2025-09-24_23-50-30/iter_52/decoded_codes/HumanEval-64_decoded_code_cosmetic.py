from typing import Sequence


def vowels_count(alpha_sequence: Sequence[str]) -> int:
    allowed_chars = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def count_helper(seq: Sequence[str], index: int, accumulator: int) -> int:
        if index == len(seq):
            return accumulator
        is_char_vowel = 1 if seq[index] in allowed_chars else 0
        return count_helper(seq, index + 1, accumulator + is_char_vowel)

    total_vowels = count_helper(alpha_sequence, 0, 0)

    if alpha_sequence and alpha_sequence[-1] in ('y', 'Y'):
        total_vowels += 1

    return total_vowels