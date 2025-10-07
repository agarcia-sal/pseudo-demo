from typing import Dict


def encode(input_text: str) -> str:
    vowels_string: str = "aeiouAEIOU"
    vowel_mappings: Dict[str, str] = {}
    index: int = 0  # zero-based index for Python strings

    while index < len(vowels_string):
        current_char: str = vowels_string[index]
        vowel_mappings[current_char] = chr(ord(current_char) + 2)
        index += 1

    toggled_text: str = ""
    position: int = 0

    while position < len(input_text):
        ch: str = input_text[position]
        if ch.isupper():
            toggled_text += ch.lower()
        elif ch.islower():
            toggled_text += ch.upper()
        else:
            toggled_text += ch
        position += 1

    result_text: str = ""
    counter: int = 0

    while counter < len(toggled_text):
        current_char: str = toggled_text[counter]
        if current_char in vowel_mappings:
            result_text += vowel_mappings[current_char]
        else:
            result_text += current_char
        counter += 1

    return result_text