from typing import Dict


def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {}
    for vowel_letter in vowels:
        vowels_replace[vowel_letter] = chr(ord(vowel_letter) + 2)
    swapped_message: str = message.swapcase()
    encoded_message_chars = []
    for character in swapped_message:
        if character in vowels_replace:
            encoded_message_chars.append(vowels_replace[character])
        else:
            encoded_message_chars.append(character)
    encoded_message: str = "".join(encoded_message_chars)
    return encoded_message