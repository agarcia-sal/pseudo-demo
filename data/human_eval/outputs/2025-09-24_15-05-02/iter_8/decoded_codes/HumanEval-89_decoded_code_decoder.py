from typing import List

def encrypt(string_input: str) -> str:
    alphabet: str = 'abcdefghijklmnopqrstuvwxyz'
    output_chars: List[str] = []
    for character in string_input:
        if character in alphabet:
            original_index: int = alphabet.index(character)
            shifted_index: int = (original_index + 4) % 26
            output_chars.append(alphabet[shifted_index])
        else:
            output_chars.append(character)
    return ''.join(output_chars)