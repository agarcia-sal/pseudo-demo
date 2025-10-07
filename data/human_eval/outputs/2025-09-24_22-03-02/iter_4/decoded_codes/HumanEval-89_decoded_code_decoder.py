def encrypt(s: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = []
    for character in s:
        if character in alphabet:
            index = alphabet.index(character)
            new_index = (index + 2 * 2) % 26
            output.append(alphabet[new_index])
        else:
            output.append(character)
    return "".join(output)