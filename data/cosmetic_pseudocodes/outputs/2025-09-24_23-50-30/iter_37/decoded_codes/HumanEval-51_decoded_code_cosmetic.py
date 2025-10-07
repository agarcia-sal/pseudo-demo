from typing import Iterable

def remove_vowels(input: Iterable[str]) -> str:
    filtered_chars = [element for element in input if element.lower() not in {"a", "e", "i", "o", "u"}]
    return "".join(filtered_chars)