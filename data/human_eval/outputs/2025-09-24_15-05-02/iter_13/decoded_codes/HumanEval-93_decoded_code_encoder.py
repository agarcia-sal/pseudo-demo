def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = {vowel: chr(ord(vowel) + 2) for vowel in vowels}
    message = message.swapcase()
    return ''.join(vowels_replace[character] if character in vowels else character for character in message)