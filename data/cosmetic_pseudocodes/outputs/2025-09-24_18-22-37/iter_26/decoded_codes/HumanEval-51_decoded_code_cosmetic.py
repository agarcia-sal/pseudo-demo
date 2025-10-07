from typing import Literal


def remove_vowels(x: str) -> str:
    result: str = ""
    idx: int = 1  # 1-based index per pseudocode

    while idx <= len(x):
        char: str = x[idx - 1]  # convert 1-based to 0-based indexing
        lower_char: str = char.lower()

        if lower_char in ('a', 'e', 'i', 'o', 'u'):
            idx += 1
            continue

        result += char
        idx += 1

    return result