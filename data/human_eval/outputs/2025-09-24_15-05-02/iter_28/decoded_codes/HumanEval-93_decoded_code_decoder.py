from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {v: chr(ord(v) + 2) for v in vowels}
    message = message.swapcase()
    return "".join(vowels_replace[c] if c in vowels else c for c in message)