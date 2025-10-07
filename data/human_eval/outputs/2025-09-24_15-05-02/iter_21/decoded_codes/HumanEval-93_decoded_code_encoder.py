from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
        'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'
    }
    swapped_message: str = message.swapcase()
    encoded_message: list[str] = []
    for character in swapped_message:
        if character in vowels:
            encoded_message.append(vowels_replace[character])
        else:
            encoded_message.append(character)
    return ''.join(encoded_message)