from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    vowels_replace: Dict[str, str] = {char: chr(ord(char) + 2) for char in vowels}
    swapped_message: str = message.swapcase()
    result_chars: list[str] = []

    for char in swapped_message:
        if char in vowels_replace:
            result_chars.append(vowels_replace[char])
        else:
            result_chars.append(char)

    return ''.join(result_chars)