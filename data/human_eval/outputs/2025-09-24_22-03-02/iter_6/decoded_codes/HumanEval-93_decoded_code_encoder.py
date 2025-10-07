def encode(message) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {v: chr(ord(v) + 2) for v in vowels}
    message = message.swapcase()
    encoded_message = ''.join(vowels_replace[c] if c in vowels else c for c in message)
    return encoded_message