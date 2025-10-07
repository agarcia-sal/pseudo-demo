from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {vowel: chr(ord(vowel) + 2) for vowel in vowels}
    swapped_message: str = message.swapcase()
    encoded_message: str = ''.join(vowels_replace[char] if char in vowels else char for char in swapped_message)
    return encoded_message