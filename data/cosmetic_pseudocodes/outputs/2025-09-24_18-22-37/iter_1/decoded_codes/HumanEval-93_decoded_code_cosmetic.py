from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {}
    for character in vowels:
        shifted_char = chr(ord(character) + 2)
        vowels_replace[character] = shifted_char
    converted_message = [ch.swapcase() for ch in message]
    result = [
        vowels_replace[ch] if ch in vowels_replace else ch
        for ch in converted_message
    ]
    return "".join(result)