from typing import Dict

def encode(message: str) -> str:
    vowels: str = "aeiouAEIOU"
    replacements: Dict[str, str] = {letter: chr(ord(letter) + 2) for letter in vowels}

    swapped_message = []
    for char in message:
        if char.islower():
            swapped_message.append(char.upper())
        elif char.isupper():
            swapped_message.append(char.lower())
        else:
            swapped_message.append(char)
    swapped_message_str = "".join(swapped_message)

    result_chars = []
    for current_char in swapped_message_str:
        if current_char in vowels:
            result_chars.append(replacements[current_char])
        else:
            result_chars.append(current_char)
    return "".join(result_chars)