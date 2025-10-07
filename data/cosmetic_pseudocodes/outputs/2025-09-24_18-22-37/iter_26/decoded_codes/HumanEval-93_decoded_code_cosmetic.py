from typing import Dict


def encode(text: str) -> str:
    vowelSet: str = "AEIOUaeiou"
    jumpValue: int = 2
    altered_map: Dict[str, str] = {}
    idx: int = 0
    while idx < len(vowelSet):
        current_char: str = vowelSet[idx]
        updated_char_code: int = ord(current_char) + jumpValue
        updated_char: str = chr(updated_char_code)
        altered_map[current_char] = updated_char
        idx += 1

    toggled_text: str = ""
    pos: int = 0
    while pos < len(text):
        ch: str = text[pos]
        if 'a' <= ch <= 'z':
            toggled_ch: str = chr(ord(ch) - 32)  # lowercase to uppercase
        elif 'A' <= ch <= 'Z':
            toggled_ch = chr(ord(ch) + 32)  # uppercase to lowercase
        else:
            toggled_ch = ch
        toggled_text += toggled_ch
        pos += 1

    output_str: str = ""
    index: int = 0
    while index < len(toggled_text):
        current_char = toggled_text[index]
        if current_char in altered_map:
            output_str += altered_map[current_char]
        else:
            output_str += current_char
        index += 1

    return output_str