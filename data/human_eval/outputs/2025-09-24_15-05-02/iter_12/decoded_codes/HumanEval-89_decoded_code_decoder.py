def encrypt(input_string: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output_string = ''
    for character in input_string:
        if character in alphabet:
            original_index = alphabet.index(character)
            shifted_index = (original_index + 2 * 2) % 26
            output_string += alphabet[shifted_index]
        else:
            output_string += character
    return output_string