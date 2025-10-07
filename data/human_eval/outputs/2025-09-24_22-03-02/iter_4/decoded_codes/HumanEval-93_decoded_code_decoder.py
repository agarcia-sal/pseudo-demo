def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = {i: chr(ord(i) + 2) for i in vowels}
    message = message.swapcase()
    result = []
    for i in message:
        result.append(vowels_replace[i] if i in vowels_replace else i)
    return ''.join(result)