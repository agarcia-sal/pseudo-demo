def encode(message) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {vowel: chr(ord(vowel) + 2) for vowel in vowels}
    message = message.swapcase()
    encoded_message = ''.join(vowels_replace[char] if char in vowels else char for char in message)
    return encoded_message