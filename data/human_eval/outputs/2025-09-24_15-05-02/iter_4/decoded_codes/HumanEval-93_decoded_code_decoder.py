def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = {char: chr(ord(char) + 2) for char in vowels}
    message = message.swapcase()
    encoded_message = []
    for char in message:
        if char in vowels_replace:
            encoded_message.append(vowels_replace[char])
        else:
            encoded_message.append(char)
    return ''.join(encoded_message)