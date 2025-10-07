def encrypt(s: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = []
    shift = 4  # 2 * 2

    for char in s:
        if char in alphabet:
            original_index = alphabet.index(char)
            shifted_index = (original_index + shift) % 26
            output.append(alphabet[shifted_index])
        else:
            output.append(char)

    return ''.join(output)