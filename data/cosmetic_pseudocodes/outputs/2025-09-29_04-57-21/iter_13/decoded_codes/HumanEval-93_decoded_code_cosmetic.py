from typing import Dict

def encode(message: str) -> str:
    vowel_chars: str = "aeiouAEIOU"
    substitution_map: Dict[str, str] = {letter: chr(ord(letter) + 2) for letter in vowel_chars}

    toggled_message = []
    for ch in message:
        if ch.isupper():
            toggled_message.append(ch.lower())
        elif ch.islower():
            toggled_message.append(ch.upper())
        else:
            toggled_message.append(ch)
    toggled_message_str = "".join(toggled_message)

    result = []
    for current_char in toggled_message_str:
        if current_char in vowel_chars:
            result.append(substitution_map[current_char])
            continue
        result.append(current_char)

    return "".join(result)