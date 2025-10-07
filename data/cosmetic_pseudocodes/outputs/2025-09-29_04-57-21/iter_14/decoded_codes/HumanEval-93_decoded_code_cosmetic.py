from typing import Dict

def encode(message: str) -> str:
    vowel_chars: str = "aeiouAEIOU"
    vowel_mappings: Dict[str, str] = {}
    index: int = 0
    while index < len(vowel_chars):
        letter = vowel_chars[index]
        vowel_mappings[letter] = chr(ord(letter) + 2)
        index += 1

    toggled_message: str = ""
    idx: int = 0
    while idx < len(message):
        current = message[idx]
        if current.islower():
            toggled_message += current.upper()
        elif current.isupper():
            toggled_message += current.lower()
        else:
            toggled_message += current
        idx += 1

    output_string: str = ""
    pos: int = 0
    while pos < len(toggled_message):
        letter = toggled_message[pos]
        if letter in vowel_mappings:
            output_string += vowel_mappings[letter]
        else:
            output_string += letter
        pos += 1

    return output_string