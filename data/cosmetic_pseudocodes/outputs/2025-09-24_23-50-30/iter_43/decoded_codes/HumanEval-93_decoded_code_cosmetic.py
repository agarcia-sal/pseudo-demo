from typing import Dict


def encode(input: str) -> str:
    keys: str = "aeiouAEIOU"
    mapping: Dict[str, str] = {char_current: chr(ord(char_current) + 2) for char_current in keys}
    swapped = ''.join(
        ch.upper() if ch.islower() else ch.lower()
        for ch in input
    )
    result = ''.join(mapping.get(ch, ch) for ch in swapped)
    return result