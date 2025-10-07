from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {vowel: chr(ord(vowel) + 2) for vowel in vowels}
    swapped_message: str = message.swapcase()
    encoded_characters: list[str] = []
    for character in swapped_message:
        if character in vowels_replace:
            encoded_characters.append(vowels_replace[character])
        else:
            encoded_characters.append(character)
    return "".join(encoded_characters)