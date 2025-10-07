from typing import Dict

def encode(text: str) -> str:
    vowels_set = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowshift_map: Dict[str, str] = {}
    index_loop_cursor = 0
    while index_loop_cursor < len(vowels_set):
        current_char = vowels_set[index_loop_cursor]
        ascii_val = ord(current_char) + 2
        trans_char = chr(ascii_val)
        vowshift_map[current_char] = trans_char
        index_loop_cursor += 1

    swapped_text_chars = []
    index_cursor = 0
    while index_cursor < len(text):
        c = text[index_cursor]
        if 'A' <= c <= 'Z':
            swapped_c = chr(ord(c) + 32)
        elif 'a' <= c <= 'z':
            swapped_c = chr(ord(c) - 32)
        else:
            swapped_c = c
        swapped_text_chars.append(swapped_c)
        index_cursor += 1
    swapped_text = ''.join(swapped_text_chars)

    encoded_text_chars = []
    encode_index = 0
    while encode_index < len(swapped_text):
        current_let = swapped_text[encode_index]
        encoded_text_chars.append(vowshift_map.get(current_let, current_let))
        encode_index += 1
    encoded_text = ''.join(encoded_text_chars)

    return encoded_text