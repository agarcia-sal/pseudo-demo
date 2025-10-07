from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {i: chr(ord(i) + 2) for i in vowels}
    message = message.swapcase()
    encoded_message: str = ""
    for i in message:
        if i in vowels_replace:
            encoded_message += vowels_replace[i]
        else:
            encoded_message += i
    return encoded_message