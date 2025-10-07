from typing import List


def get_closest_vowel(word: str) -> str:
    vowels_set: List[str] = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

    def helper(i: int) -> str:
        if i > len(word) - 2:
            return ""
        curr_char = word[i]
        prev_char = word[i - 1]
        next_char = word[i + 1]
        if curr_char in vowels_set:
            if prev_char not in vowels_set and next_char not in vowels_set:
                return curr_char
            return helper(i + 1)
        return helper(i + 1)

    if len(word) < 3:
        return ""
    return helper(1)