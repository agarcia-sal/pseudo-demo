from typing import List


def remove_vowels(text: str) -> str:
    vowels: List[str] = ["a", "e", "i", "o", "u"]
    filtered_chars: List[str] = []
    for character in text:
        lower_char = character.lower()
        if lower_char not in vowels:
            filtered_chars.append(character)
    return "".join(filtered_chars)