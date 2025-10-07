from typing import List

def encrypt(string_input: str) -> str:
    alphabet_string: str = 'abcdefghijklmnopqrstuvwxyz'
    output_chars: List[str] = []
    for character in string_input:
        if character in alphabet_string:
            shifted_index: int = (alphabet_string.index(character) + 2 * 2) % 26
            output_chars.append(alphabet_string[shifted_index])
        else:
            output_chars.append(character)
    return ''.join(output_chars)