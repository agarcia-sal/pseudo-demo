from typing import List


def remove_vowels(text: str) -> str:
    filtered_chars: List[str] = []
    idx: int = 0
    while idx < len(text):
        current_char: str = text[idx]
        lower_char: str = current_char.lower()
        if lower_char not in {"a", "e", "i", "o", "u"}:
            filtered_chars.append(current_char)
        idx += 1
    return "".join(filtered_chars)