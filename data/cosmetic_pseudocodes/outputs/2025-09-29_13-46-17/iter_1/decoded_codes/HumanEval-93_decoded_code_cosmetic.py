from typing import Dict


def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {}
    for ch in vowels:
        vowels_replace[ch] = chr(ord(ch) + 2)
    swapped_message: str = ""
    for ch in message:
        if ch.isupper():
            swapped_message += ch.lower()
        elif ch.islower():
            swapped_message += ch.upper()
        else:
            swapped_message += ch
    result: str = ""
    for ch in swapped_message:
        if ch in vowels_replace:
            result += vowels_replace[ch]
        else:
            result += ch
    return result