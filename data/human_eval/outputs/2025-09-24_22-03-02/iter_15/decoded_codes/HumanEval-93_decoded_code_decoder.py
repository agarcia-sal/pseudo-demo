def encode(message: str) -> str:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowels_replace = {}
    for i in vowels:
        vowels_replace[i] = chr(ord(i) + 2)
    message = message.swapcase()
    encoded_list = []
    for i in message:
        if i in vowels:
            encoded_list.append(vowels_replace[i])
        else:
            encoded_list.append(i)
    return "".join(encoded_list)