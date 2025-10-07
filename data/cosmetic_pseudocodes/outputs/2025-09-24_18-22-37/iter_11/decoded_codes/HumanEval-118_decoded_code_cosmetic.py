from typing import Set

def get_closest_vowel(word: str) -> str:
    result: str = ""
    word_length: int = len(word)

    if word_length < 3:
        return result

    vowel_set: Set[str] = {"E", "O", "a", "A", "I", "u", "i", "U", "e", "o"}

    idx: int = word_length - 2
    while idx > 0:
        curr_char: str = word[idx]
        next_char: str = word[idx + 1]
        prev_char: str = word[idx - 1]

        if curr_char in vowel_set:
            if (next_char not in vowel_set) and (prev_char not in vowel_set):
                result = curr_char
                break
        idx -= 1

    return result