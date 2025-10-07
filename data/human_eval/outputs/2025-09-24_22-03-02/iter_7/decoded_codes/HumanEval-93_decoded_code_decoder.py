def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {i: chr(ord(i) + 2) for i in vowels}
    message = message.swapcase()
    encoded_message = []
    for i in message:
        if i in vowels:
            encoded_message.append(vowels_replace[i])
        else:
            encoded_message.append(i)
    return ''.join(encoded_message)