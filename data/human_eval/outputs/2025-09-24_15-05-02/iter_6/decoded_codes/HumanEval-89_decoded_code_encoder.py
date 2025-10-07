def encrypt(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output_string = ""
    for character in input_string:
        if character in alphabet:
            original_index = alphabet.index(character)
            new_index = (original_index + 4) % 26
            output_string += alphabet[new_index]
        else:
            output_string += character
    return output_string