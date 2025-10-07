def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {i: chr(ord(i) + 2) for i in vowels}
    message = message.swapcase()
    return ''.join(vowels_replace[i] if i in vowels else i for i in message)