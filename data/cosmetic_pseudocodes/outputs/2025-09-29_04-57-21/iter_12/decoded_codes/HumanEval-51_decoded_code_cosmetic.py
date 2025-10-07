from typing import List

def remove_vowels(text: str) -> str:
    filtered_chars: List[str] = []

    index: int = 0
    while index < len(text):
        current_char: str = text[index]
        lowercase_char: str = current_char.lower()

        if lowercase_char in {'a', 'e', 'i', 'o', 'u'}:
            index += 1
            continue

        filtered_chars.append(current_char)
        index += 1

    return "".join(filtered_chars)