from typing import List

def get_closest_vowel(word: str) -> str:
    vowels_list: List[str] = ["a", "e", "i", "o", "u", "A", "E", "O", "U", "I"]

    def is_vowel(char: str) -> bool:
        return char in vowels_list

    def search(pos: int) -> str:
        if pos < 1:
            return ""
        if (
            is_vowel(word[pos])
            and not is_vowel(word[pos + 1])
            and not is_vowel(word[pos - 1])
        ):
            return word[pos]
        return search(pos - 1)

    if len(word) < 3:
        return ""
    return search(len(word) - 2)