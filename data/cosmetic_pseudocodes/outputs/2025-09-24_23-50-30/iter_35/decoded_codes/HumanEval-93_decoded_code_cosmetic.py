from typing import Dict

def encode(input_data: str) -> str:
    key_chars = list("aeiouAEIOU")
    substitution_map: Dict[str, str] = {}
    for char_key in key_chars:
        ascii_val = ord(char_key)
        substitution_map[char_key] = chr(ascii_val + 2)

    toggled_data = []
    for curr_char in input_data:
        if 'A' <= curr_char <= 'Z':
            toggled_data.append(chr(ord(curr_char) + 32))  # uppercase to lowercase
        elif 'a' <= curr_char <= 'z':
            toggled_data.append(chr(ord(curr_char) - 32))  # lowercase to uppercase
        else:
            toggled_data.append(curr_char)
    toggled_data_str = ''.join(toggled_data)

    output_chars = []
    for ch in toggled_data_str:
        replacement_char = substitution_map.get(ch)
        if replacement_char is not None:
            output_chars.append(replacement_char)
        else:
            output_chars.append(ch)

    return ''.join(output_chars)