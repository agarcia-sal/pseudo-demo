from typing import List

def remove_vowels(phrase: str) -> str:
    filtered_chars: List[str] = []
    idx: int = 0
    while idx < len(phrase):
        current_char: str = phrase[idx]
        lower_char: str = current_char.lower()
        is_vowel: bool = lower_char in ('a', 'e', 'i', 'o', 'u')
        if not is_vowel:
            filtered_chars.append(current_char)
        idx += 1

    result_str: str = ''
    pos: int = 0
    while pos < len(filtered_chars):
        result_str += filtered_chars[pos]
        pos += 1

    return result_str