from typing import List


def encrypt(input_string: str) -> str:
    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    output_chars: List[str] = []
    for character in input_string:
        if character in alphabet:
            shifted_index: int = (alphabet.index(character) + 2 * 2) % 26
            output_chars.append(alphabet[shifted_index])
        else:
            output_chars.append(character)
    return ''.join(output_chars)