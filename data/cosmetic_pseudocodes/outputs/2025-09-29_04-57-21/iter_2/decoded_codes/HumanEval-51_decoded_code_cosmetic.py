from typing import List


def remove_vowels(text: str) -> str:
    filtered_chars: List[str] = []
    for character in text:
        lower_char = character.lower()
        if not (lower_char == "a" or lower_char == "e" or lower_char == "i" or lower_char == "o" or lower_char == "u"):
            filtered_chars.append(character)
    result_text = ""
    for element in filtered_chars:
        result_text += element
    return result_text