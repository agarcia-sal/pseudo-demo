from typing import Dict


def encode(message_input: str) -> str:
    vowels_list: str = "AEIOUaeiou"
    replacement_map: Dict[str, str] = {}
    index_counter: int = 0
    while index_counter < len(vowels_list):
        current_char: str = vowels_list[index_counter]
        ascii_original: int = ord(current_char)
        ascii_shifted: int = ascii_original + 0x2  # shift by 2
        replacement_char: str = chr(ascii_shifted)
        replacement_map[current_char] = replacement_char
        index_counter += 1

    swapped_message: str = ""
    position: int = 0
    while position < len(message_input):
        char_in_message: str = message_input[position]

        if 'a' <= char_in_message <= 'z':
            uppercase_equiv: str = chr(ord(char_in_message) - 0x20)
            swapped_char: str = uppercase_equiv
        elif 'A' <= char_in_message <= 'Z':
            lowercase_equiv: str = chr(ord(char_in_message) + 0x20)
            swapped_char: str = lowercase_equiv
        else:
            swapped_char = char_in_message

        swapped_message += swapped_char
        position += 1

    encoded_message: str = ""
    iterator_pos: int = 0

    while iterator_pos < len(swapped_message):
        current_symbol: str = swapped_message[iterator_pos]

        if current_symbol in replacement_map:
            encoded_message += replacement_map[current_symbol]
        else:
            encoded_message += current_symbol

        iterator_pos += 1

    return encoded_message