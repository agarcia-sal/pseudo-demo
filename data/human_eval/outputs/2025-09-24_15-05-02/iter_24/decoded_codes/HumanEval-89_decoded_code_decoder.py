from typing import List

def encrypt(string_input: str) -> str:
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    output_string: List[str] = []
    for character in string_input:
        if character in alphabet:
            original_index: int = alphabet.index(character)
            shifted_index: int = (original_index + 4) % 26
            output_string.append(alphabet[shifted_index])
        else:
            output_string.append(character)
    return "".join(output_string)