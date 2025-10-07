from typing import Dict

def encode(orig_message: str) -> str:
    alt_vowels: str = "aeiouAEIOU"
    replacement_map: Dict[str, str] = {}

    for current_char in alt_vowels:
        substitute_char = chr(ord(current_char) + 2)
        replacement_map[current_char] = substitute_char

    flipped_message = []
    for current_char in orig_message:
        if 'A' <= current_char <= 'Z':
            flipped_message.append(chr(ord(current_char) + 32))
        elif 'a' <= current_char <= 'z':
            flipped_message.append(chr(ord(current_char) - 32))
        else:
            flipped_message.append(current_char)
    flipped_message_str = ''.join(flipped_message)

    output_message = []
    for current_char in flipped_message_str:
        if current_char in replacement_map:
            output_message.append(replacement_map[current_char])
        else:
            output_message.append(current_char)

    return ''.join(output_message)