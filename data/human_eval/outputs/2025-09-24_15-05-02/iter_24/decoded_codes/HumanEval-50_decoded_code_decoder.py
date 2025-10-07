from typing import Union

def encode_shift(input_string: str) -> str:
    # Shift each lowercase letter by 5 positions in the alphabet, wrapping around
    result_chars = []
    for character in input_string:
        if 'a' <= character <= 'z':
            shifted_code = ((ord(character) + 5 - ord('a')) % 26) + ord('a')
            result_chars.append(chr(shifted_code))
        else:
            # Preserve characters outside a-z as is (implicit in pseudocode context)
            result_chars.append(character)
    return ''.join(result_chars)

def decode_shift(encoded_string: str) -> str:
    # Reverse the shift by 5 positions, wrapping around
    result_chars = []
    for character in encoded_string:
        if 'a' <= character <= 'z':
            shifted_code = ((ord(character) - 5 - ord('a')) % 26) + ord('a')
            result_chars.append(chr(shifted_code))
        else:
            # Preserve characters outside a-z
            result_chars.append(character)
    return ''.join(result_chars)