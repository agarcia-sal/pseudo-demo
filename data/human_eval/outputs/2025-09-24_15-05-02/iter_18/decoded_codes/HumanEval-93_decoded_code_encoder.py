from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {v: chr(ord(v) + 2) for v in vowels}
    swapped_message: str = message.swapcase()
    return ''.join(vowels_replace[i] if i in vowels_replace else i for i in swapped_message)