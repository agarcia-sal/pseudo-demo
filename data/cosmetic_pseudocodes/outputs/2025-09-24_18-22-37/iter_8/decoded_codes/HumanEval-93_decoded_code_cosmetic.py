from typing import Dict


def encode(input_string: str) -> str:
    vowel_set: str = "AEIOUaeiou"
    translation_map: Dict[str, str] = {}

    for current_char in vowel_set:
        translation_map[current_char] = chr(ord(current_char) + 2)

    swapped_string = ''.join(
        ch.upper() if ch.islower() else ch.lower()
        for ch in input_string
    )

    result_chars = [
        translation_map[ch] if ch in vowel_set else ch
        for ch in swapped_string
    ]

    return ''.join(result_chars)