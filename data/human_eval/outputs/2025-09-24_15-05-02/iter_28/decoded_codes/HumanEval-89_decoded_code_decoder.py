from typing import Optional


def encrypt(s: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output_string = []
    for character in s:
        if character in alphabet:
            shifted_index = (alphabet.index(character) + 4) % 26
            output_string.append(alphabet[shifted_index])
        else:
            output_string.append(character)
    return "".join(output_string)