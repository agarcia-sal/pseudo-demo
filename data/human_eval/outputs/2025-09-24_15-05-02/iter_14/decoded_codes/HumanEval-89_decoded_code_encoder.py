def encrypt(input_string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output_string = ''
    for character in input_string:
        if character in alphabet:
            new_index = (alphabet.index(character) + 2 * 2) % 26
            output_string += alphabet[new_index]
        else:
            output_string += character
    return output_string