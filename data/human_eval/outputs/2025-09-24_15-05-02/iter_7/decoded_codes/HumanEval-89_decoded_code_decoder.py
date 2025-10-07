def encrypt(input_string: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output_string = []
    for character in input_string:
        if character in alphabet:
            new_index = (alphabet.index(character) + 4) % 26
            output_string.append(alphabet[new_index])
        else:
            output_string.append(character)
    return ''.join(output_string)