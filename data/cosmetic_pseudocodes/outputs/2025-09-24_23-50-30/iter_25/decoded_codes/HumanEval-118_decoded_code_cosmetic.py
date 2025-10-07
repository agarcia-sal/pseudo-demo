from typing import List


def get_closest_vowel(str: str) -> str:
    if len(str) < 3:
        return ""

    vowel_collection: List[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    curr_pos: int = len(str) - 2
    while curr_pos >= 1:
        if str[curr_pos] in vowel_collection:
            if str[curr_pos + 1] not in vowel_collection and str[curr_pos - 1] not in vowel_collection:
                return str[curr_pos]
        curr_pos -= 1

    return ""