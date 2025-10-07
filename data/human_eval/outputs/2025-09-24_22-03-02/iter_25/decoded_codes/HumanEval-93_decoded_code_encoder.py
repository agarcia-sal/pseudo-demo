def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {c: chr(ord(c) + 2) for c in vowels}
    swapped_message = []
    for c in message:
        if 'a' <= c <= 'z':
            swapped_message.append(chr(ord(c) - 32))
        elif 'A' <= c <= 'Z':
            swapped_message.append(chr(ord(c) + 32))
        else:
            swapped_message.append(c)
    swapped_message = ''.join(swapped_message)
    encoded_message = []
    for c in swapped_message:
        if c in vowels:
            encoded_message.append(vowels_replace[c])
        else:
            encoded_message.append(c)
    return ''.join(encoded_message)