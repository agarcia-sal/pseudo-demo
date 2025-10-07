from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {v: chr(ord(v) + 2) for v in vowels}
    message = message.swapcase()
    encoded_message = []
    for character in message:
        if character in vowels:
            encoded_message.append(vowels_replace[character])
        else:
            encoded_message.append(character)
    return "".join(encoded_message)