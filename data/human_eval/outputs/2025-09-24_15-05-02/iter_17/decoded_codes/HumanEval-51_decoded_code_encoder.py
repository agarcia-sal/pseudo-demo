from typing import List

def remove_vowels(text: str) -> str:
    vowels: List[str] = ["a", "e", "i", "o", "u"]
    result_characters: List[str] = []
    for character in text:
        if character.lower() not in vowels:
            result_characters.append(character)
    result: str = "".join(result_characters)
    return result