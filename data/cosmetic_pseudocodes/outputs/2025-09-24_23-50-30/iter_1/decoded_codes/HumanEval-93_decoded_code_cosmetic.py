from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {char: chr(ord(char) + 2) for char in vowels}
    swapped_message: str = "".join(
        letter.lower() if letter.isupper() else letter.upper() if letter.islower() else letter
        for letter in message
    )
    result: str = "".join(vowels_replace.get(ch, ch) for ch in swapped_message)
    return result