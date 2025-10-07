from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {
        vowel: chr(ord(vowel) + 2) for vowel in vowels
    }
    swapped_message: str = message.swapcase()
    return "".join(
        vowels_replace.get(char, char) for char in swapped_message
    )