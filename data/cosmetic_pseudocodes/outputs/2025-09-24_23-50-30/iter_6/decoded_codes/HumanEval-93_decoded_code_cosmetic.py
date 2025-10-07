from typing import Dict

def encode(message: str) -> str:
    vowel_collection: str = "aeiouAEIOU"
    replacement_map: Dict[str, str] = {}
    idx: int = 0
    while idx < len(vowel_collection):
        ch = vowel_collection[idx]
        replacement_map[ch] = chr(ord(ch) + 2)
        idx += 1

    toggled_message: str = ""
    pos: int = 0
    while pos < len(message):
        current_char = message[pos]
        if 'a' <= current_char <= 'z':
            toggled_message += chr(ord(current_char) - 32)  # lowercase to uppercase
        elif 'A' <= current_char <= 'Z':
            toggled_message += chr(ord(current_char) + 32)  # uppercase to lowercase
        else:
            toggled_message += current_char
        pos += 1

    output_string: str = ""
    index: int = 0
    while index < len(toggled_message):
        element = toggled_message[index]
        if element in replacement_map:
            output_string += replacement_map[element]
        else:
            output_string += element
        index += 1

    return output_string