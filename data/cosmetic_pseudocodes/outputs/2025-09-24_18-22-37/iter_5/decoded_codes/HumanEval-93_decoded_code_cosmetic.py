from typing import Dict

def encode(input_text: str) -> str:
    vowel_letters: str = "aeiouAEIOU"
    vowel_mapping: Dict[str, str] = {}
    index_counter: int = 0
    while index_counter < len(vowel_letters):
        current_char: str = vowel_letters[index_counter]
        ascii_val: int = ord(current_char)
        mapped_char: str = chr(ascii_val + 2)
        vowel_mapping[current_char] = mapped_char
        index_counter += 1

    swapped_text: str = ""
    iterator: int = 0
    while iterator < len(input_text):
        cur_char: str = input_text[iterator]
        if 'a' <= cur_char <= 'z':
            swapped_char: str = chr(ord(cur_char) - 32)
        elif 'A' <= cur_char <= 'Z':
            swapped_char = chr(ord(cur_char) + 32)
        else:
            swapped_char = cur_char
        swapped_text += swapped_char
        iterator += 1

    result_string: str = ""
    pos: int = 0
    while pos < len(swapped_text):
        letter: str = swapped_text[pos]
        if letter in vowel_mapping:
            result_string += vowel_mapping[letter]
        else:
            result_string += letter
        pos += 1

    return result_string