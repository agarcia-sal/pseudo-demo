from typing import Dict


def encode(input_text: str) -> str:
    vowels_var: str = "aeiouAEIOU"
    vowels_map: Dict[str, str] = {}
    i: int = 0
    while i < len(vowels_var):
        key_char: str = vowels_var[i]
        ascii_val: int = ord(key_char)
        ascii_new: int = ascii_val + 2  # + (1 + 1)
        value_char: str = chr(ascii_new)
        vowels_map[key_char] = value_char
        i += 1

    converted_text: str = ""
    j: int = 0
    total_chars: int = len(input_text)
    while j < total_chars:
        ch: str = input_text[j]
        if ch == ch.lower():
            swapped_ch: str = ch.upper()
        elif ch == ch.upper():
            swapped_ch = ch.lower()
        else:
            swapped_ch = ch

        temp_char: str = swapped_ch
        temp_result: str = vowels_map[temp_char] if temp_char in vowels_map else temp_char
        converted_text += temp_result
        j += 1

    return converted_text