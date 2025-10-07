from typing import Dict


def encode(input_text: str) -> str:
    letters_set: str = "AEIOUaeiou"
    shifted_mapping: Dict[str, str] = {}
    idx: int = 0
    while idx < len(letters_set):
        current_symbol: str = letters_set[idx]
        original_code: int = ord(current_symbol)
        incremented_code: int = original_code + 0x2
        substitute_symbol: str = chr(incremented_code)
        shifted_mapping[current_symbol] = substitute_symbol
        idx += 1

    toggled_text: str = ""
    pos: int = 0

    while pos < len(input_text):
        char_orig: str = input_text[pos]
        if 'a' <= char_orig <= 'z':
            char_upper_code: int = ord(char_orig) - 0x20
            toggled_char: str = chr(char_upper_code)
            toggled_text += toggled_char
        elif 'A' <= char_orig <= 'Z':
            char_lower_code: int = ord(char_orig) + 32
            toggled_char = chr(char_lower_code)
            toggled_text += toggled_char
        else:
            toggled_text += char_orig
        pos += 1

    result_text: str = ""
    index_var: int = 0

    while index_var < len(toggled_text):
        current_char: str = toggled_text[index_var]
        if current_char in shifted_mapping:
            mapped_char: str = shifted_mapping[current_char]
            result_text += mapped_char
        else:
            result_text += current_char
        index_var += 1

    return result_text