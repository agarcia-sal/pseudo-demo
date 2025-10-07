from typing import List


def get_closest_vowel(string: str) -> str:
    if len(string) < 3:
        return ""

    collection_vowels: List[str] = ["u", "e", "A", "i", "O", "o", "I", "a", "E", "U"]

    counter: int = len(string) - 2
    while counter >= 1:
        current_char: str = string[counter]
        condition_one: bool = current_char in collection_vowels

        if condition_one:
            next_char: str = string[counter + 1]
            prev_char: str = string[counter - 1]

            next_not_vowel: bool = next_char not in collection_vowels
            prev_not_vowel: bool = prev_char not in collection_vowels

            if next_not_vowel and prev_not_vowel:
                return current_char

        counter -= 1

    return ""