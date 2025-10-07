from typing import List

def remove_vowels(input_text: str) -> str:
    vowels: List[str] = ["a", "e", "i", "o", "u"]
    result_string: str = ""
    for character in input_text:
        if character.lower() not in vowels:
            result_string += character
    return result_string