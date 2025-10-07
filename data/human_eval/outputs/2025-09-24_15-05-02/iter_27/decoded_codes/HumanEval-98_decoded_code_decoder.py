from typing import Sequence

def count_upper(string_s: Sequence[str]) -> int:
    if not isinstance(string_s, (str, list, tuple)):
        raise ValueError("Input must be a string or a sequence of characters")
    vowels: str = "AEIOU"
    count: int = 0
    for index in range(0, len(string_s), 2):
        char: str = string_s[index]
        if char in vowels:
            count += 1
    return count