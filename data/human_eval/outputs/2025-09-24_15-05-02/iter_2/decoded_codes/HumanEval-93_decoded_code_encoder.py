def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    for i in vowels:
        vowels_replace[i] = chr(ord(i) + 2)
    message = message.swapcase()
    result = ""
    for i in message:
        if i in vowels:
            result += vowels_replace[i]
        else:
            result += i
    return result