def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {v: chr(ord(v) + 2) for v in vowels}
    message = message.swapcase()
    return ''.join(vowels_replace[c] if c in vowels_replace else c for c in message)