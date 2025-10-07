from typing import List

def remove_vowels(message: str) -> str:
    result: List[str] = []
    index: int = 0

    while index < len(message):
        current_char: str = message[index]
        if current_char.lower() not in {"a", "e", "i", "o", "u"}:
            result.append(current_char)
        index += 1

    return "".join(result)