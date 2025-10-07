from typing import Set


def get_closest_vowel(sequence: str) -> str:
    if len(sequence) <= 2:
        return ""

    vowel_set: Set[str] = {"u", "E", "i", "A", "O", "o", "a", "e", "U", "I"}

    for pos in range(len(sequence) - 2, 0, -1):
        if sequence[pos] in vowel_set:
            if (sequence[pos + 1] not in vowel_set) and (sequence[pos - 1] not in vowel_set):
                return sequence[pos]

    return ""