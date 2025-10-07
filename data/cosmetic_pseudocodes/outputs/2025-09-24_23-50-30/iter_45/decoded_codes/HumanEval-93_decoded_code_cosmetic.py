from typing import Dict, Set

def encode(message: str) -> str:
    lookup_vowels: Set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    substitution_map: Dict[str, str] = {}
    for item in lookup_vowels:
        code_point = ord(item)
        substitution_map[item] = chr(code_point + 2)

    toggled_message = []
    for current_char in message:
        if current_char.isupper():
            toggled_message.append(current_char.lower())
        else:
            toggled_message.append(current_char.upper())
    toggled_message_str = ''.join(toggled_message)

    altered_message = [
        substitution_map[char_candidate] if char_candidate in lookup_vowels else char_candidate
        for char_candidate in toggled_message_str
    ]

    return ''.join(altered_message)