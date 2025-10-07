from typing import List

def remove_vowels(text: str) -> str:
    result_characters: List[str] = []
    for character in text:
        if character.lower() not in {"a", "e", "i", "o", "u"}:
            result_characters.append(character)
    result_string: str = "".join(result_characters)
    return result_string