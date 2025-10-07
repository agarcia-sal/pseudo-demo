from typing import Callable

def remove_vowels(text: str) -> str:
    forbidden_set = {"a", "e", "i", "o", "u"}

    def traverse(index: int, accumulator: str) -> str:
        if index == len(text):
            return accumulator
        current_char = text[index]
        if current_char.lower() not in forbidden_set:
            return traverse(index + 1, accumulator + current_char)
        else:
            return traverse(index + 1, accumulator)

    return traverse(0, "")