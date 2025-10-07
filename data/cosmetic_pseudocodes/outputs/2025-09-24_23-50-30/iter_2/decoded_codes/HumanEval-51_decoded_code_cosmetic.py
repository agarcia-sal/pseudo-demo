from typing import Set

def remove_vowels(text: str) -> str:
    result: str = ""
    vowels: Set[str] = {"a", "e", "i", "o", "u"}
    for index in range(len(text) - 1, -1, -1):
        if text[index].lower() in vowels:
            continue
        result = text[index] + result
    return result