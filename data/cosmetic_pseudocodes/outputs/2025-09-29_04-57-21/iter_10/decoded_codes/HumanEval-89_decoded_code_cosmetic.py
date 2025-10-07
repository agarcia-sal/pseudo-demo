from typing import Literal


def encrypt(input_string: str) -> str:
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    result: str = ""
    position: int = 0
    length_input: int = len(input_string)

    while position < length_input:
        current_char: str = input_string[position]

        if current_char not in alphabet:
            result += current_char
            position += 1
            continue

        index_in_alphabet: int = 0
        found: bool = False

        while index_in_alphabet < len(alphabet) and not found:
            if alphabet[index_in_alphabet] == current_char:
                found = True
            else:
                index_in_alphabet += 1

        shifted: int = (index_in_alphabet + 4) % 26
        result += alphabet[shifted]

        position += 1

    return result