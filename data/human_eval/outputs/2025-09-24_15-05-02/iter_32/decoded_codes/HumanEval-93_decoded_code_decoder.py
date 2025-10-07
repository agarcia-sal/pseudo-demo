from typing import Dict


def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {ch: chr(ord(ch) + 2) for ch in vowels}
    message = message.swapcase()
    return "".join(vowels_replace[c] if c in vowels_replace else c for c in message)