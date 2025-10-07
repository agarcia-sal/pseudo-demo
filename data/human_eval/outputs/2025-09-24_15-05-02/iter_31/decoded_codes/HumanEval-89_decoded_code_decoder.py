from typing import AnyStr

def encrypt(string_input: AnyStr) -> str:
    alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
    output_string = []
    for character in string_input:
        if character in alphabet_string:
            shifted_index = (alphabet_string.index(character) + 2 * 2) % 26
            output_string.append(alphabet_string[shifted_index])
        else:
            output_string.append(character)
    return ''.join(output_string)