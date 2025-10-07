from typing import List


def remove_vowels(phrase: str) -> str:
    idx: int = 0
    filtered_chars: List[str] = []
    while idx < len(phrase):
        ch: str = phrase[idx]
        if ch.lower() in {'a', 'e', 'i', 'o', 'u'}:
            idx += 1
            continue
        filtered_chars.append(ch)
        idx += 1
    result: str = ''
    for elem in filtered_chars:
        result += elem
    return result