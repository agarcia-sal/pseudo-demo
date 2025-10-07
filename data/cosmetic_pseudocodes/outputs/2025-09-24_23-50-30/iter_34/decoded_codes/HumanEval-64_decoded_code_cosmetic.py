from typing import Set


def vowels_count(alpha: str) -> int:
    vowels_map: Set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def count_helper(pos: int, tally: int) -> int:
        if pos > len(alpha):
            return tally
        letter = alpha[pos - 1]  # pos is 1-based
        is_vowel = 1 if letter in vowels_map else 0
        return count_helper(pos + 1, tally + is_vowel)

    total = count_helper(1, 0)

    last_char = alpha[-1] if alpha else ''
    if not (last_char != 'y' and last_char != 'Y'):
        total += 1

    return total