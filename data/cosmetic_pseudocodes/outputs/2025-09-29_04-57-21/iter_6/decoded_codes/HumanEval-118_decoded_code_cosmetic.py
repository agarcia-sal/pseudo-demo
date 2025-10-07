from typing import Set


def get_closest_vowel(term: str) -> str:
    if len(term) < 3:
        return ""

    vowel_set: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    position = len(term) - 2
    while position >= 1:
        if term[position] in vowel_set:
            if (term[position + 1] not in vowel_set) and (term[position - 1] not in vowel_set):
                return term[position]
        position -= 1

    return ""