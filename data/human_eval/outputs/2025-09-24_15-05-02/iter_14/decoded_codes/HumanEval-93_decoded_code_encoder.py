def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = {char: chr(ord(char) + 2) for char in vowels}
    message = message.swapcase()
    return ''.join(vowels_replace[char] if char in vowels_replace else char for char in message)