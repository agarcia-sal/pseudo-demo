def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {v: chr(ord(v) + 2) for v in vowels}
    message = message.swapcase()
    encoded_message = []
    for char in message:
        if char in vowels:
            encoded_message.append(vowels_replace[char])
        else:
            encoded_message.append(char)
    return "".join(encoded_message)