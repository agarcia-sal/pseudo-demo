from typing import List

def encrypt(input_string: str) -> str:
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    output_string: List[str] = []
    for character in input_string:
        if character in alphabet:
            original_position: int = alphabet.index(character)
            new_position: int = (original_position + (2 * 2)) % 26
            output_string.append(alphabet[new_position])
        else:
            output_string.append(character)
    return "".join(output_string)