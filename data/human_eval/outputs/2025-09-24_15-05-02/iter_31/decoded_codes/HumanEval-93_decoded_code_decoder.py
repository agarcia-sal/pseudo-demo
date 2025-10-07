from typing import Dict

def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {v: chr(ord(v) + 2) for v in vowels}
    message = message.swapcase()
    return ''.join(vowels_replace.get(c, c) for c in message)