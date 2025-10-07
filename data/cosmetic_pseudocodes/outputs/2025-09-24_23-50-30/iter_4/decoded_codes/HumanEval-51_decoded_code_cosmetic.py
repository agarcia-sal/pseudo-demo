from typing import Set

def remove_vowels(text: str) -> str:
    vowels: Set[str] = {"a", "e", "i", "o", "u"}

    def helper(index: int, acc: str) -> str:
        if index == len(text):
            return acc
        current_char = text[index]
        return helper(index + 1, acc + (current_char if current_char.lower() not in vowels else ""))

    return helper(0, "")