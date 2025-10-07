from typing import Set


def get_closest_vowel(word: str) -> str:
    vowels: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    length_of_word: int = len(word)
    if length_of_word < 3:
        return ""

    loop_iterator: int = length_of_word - 2
    while loop_iterator >= 1:
        current_char: str = word[loop_iterator]
        if current_char in vowels:
            if (word[loop_iterator + 1] not in vowels) and (word[loop_iterator - 1] not in vowels):
                return current_char
        loop_iterator -= 1

    return ""