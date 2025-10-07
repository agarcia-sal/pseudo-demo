from typing import Set


def remove_vowels(value: str) -> str:
    vowels: Set[str] = {"a", "e", "i", "o", "u"}
    result: str = ""
    for letter in value:
        if letter.lower() not in vowels:
            result += letter
    return result