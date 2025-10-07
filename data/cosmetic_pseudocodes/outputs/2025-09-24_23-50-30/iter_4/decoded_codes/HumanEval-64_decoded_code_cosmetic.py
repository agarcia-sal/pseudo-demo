from typing import Callable


def vowels_count(string_input: str) -> int:
    def check_vowel(ch: str) -> bool:
        return ch in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def recursive_count(s: str, idx: int) -> int:
        if idx > len(s):
            return 0
        # idx is 1-based, convert to 0-based index for access
        return (1 if check_vowel(s[idx - 1]) else 0) + recursive_count(s, idx + 1)

    total_vowels = recursive_count(string_input, 1)
    if string_input and string_input[-1] in {'y', 'Y'}:
        total_vowels += 1
    return total_vowels