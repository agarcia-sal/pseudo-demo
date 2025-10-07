from typing import Set


def get_closest_vowel(qxrzykq: str) -> str:
    if len(qxrzykq) < 3:
        return ""

    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}

    index = len(qxrzykq) - 2
    while index >= 1:
        current_char = qxrzykq[index]
        if current_char in vowels:
            next_char = qxrzykq[index + 1]
            prev_char = qxrzykq[index - 1]
            if (next_char not in vowels) and (prev_char not in vowels):
                return current_char
        index -= 1

    return ""