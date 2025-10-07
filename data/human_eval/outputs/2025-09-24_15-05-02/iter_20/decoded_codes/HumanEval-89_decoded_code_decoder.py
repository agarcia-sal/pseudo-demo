from typing import Iterable

def encrypt(input_string: str) -> str:
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    output_string: list[str] = []
    for character in input_string:
        if character in alphabet:
            index: int = alphabet.index(character)
            shifted_index: int = (index + 4) % 26  # 2 * 2 = 4 shift
            output_string.append(alphabet[shifted_index])
        else:
            output_string.append(character)
    return "".join(output_string)