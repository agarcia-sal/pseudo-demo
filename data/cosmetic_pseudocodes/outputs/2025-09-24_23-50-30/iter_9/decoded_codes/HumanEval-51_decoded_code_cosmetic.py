from typing import List


def remove_vowels(input_str: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result_chars: List[str] = [
        ch for ch in input_str if ch.lower() not in vowels
    ]
    return ''.join(result_chars)