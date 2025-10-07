def encode(message):
    vowels = "aeiouAEIOU"
    vowelsReplace = {v: chr(ord(v) + 2) for v in vowels}
    message = message.swapcase()
    return ''.join(vowelsReplace[c] if c in vowelsReplace else c for c in message)