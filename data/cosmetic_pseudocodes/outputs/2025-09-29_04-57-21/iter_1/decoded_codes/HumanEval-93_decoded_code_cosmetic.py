from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    shift_map: Dict[str, str] = {letter: chr(ord(letter) + 2) for letter in vowels}
    toggled_message = ''.join(
        ch.upper() if ch.islower() else ch.lower() if ch.isupper() else ch
        for ch in message
    )
    result = ''.join(shift_map[char] if char in shift_map else char for char in toggled_message)
    return result