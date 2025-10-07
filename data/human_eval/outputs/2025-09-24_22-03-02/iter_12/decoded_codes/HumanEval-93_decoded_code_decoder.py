def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    for i in vowels:
        vowels_replace[i] = chr(ord(i) + 2)
    message = message.swapcase()
    return ''.join(vowels_replace[i] if i in vowels_replace else i for i in message)