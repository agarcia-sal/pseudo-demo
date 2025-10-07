from typing import Dict

def encode(message: str) -> str:
    reference_vowels: list[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    translation_map: Dict[str, str] = {}

    # Map each vowel char to itself shifted by 2 in Unicode code points
    for current_char in reference_vowels:
        mapped_char = chr(ord(current_char) + 2)
        translation_map[current_char] = mapped_char

    swapped_message: str = ""
    for ch in message:
        upper_flag = ch != ch.lower()
        if upper_flag:
            swapped_message += ch.lower()
        else:
            swapped_message += ch.upper()

    result_string: str = ""
    for each_character in swapped_message:
        if each_character in translation_map:
            result_string += translation_map[each_character]
        else:
            result_string += each_character

    return result_string