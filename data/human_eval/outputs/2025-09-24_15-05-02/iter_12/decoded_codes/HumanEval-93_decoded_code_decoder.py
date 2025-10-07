def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {vowel: chr(ord(vowel) + 2) for vowel in vowels}
    message = message.swapcase()
    encoded_message = ""
    for character in message:
        if character in vowels:
            encoded_message += vowels_replace[character]
        else:
            encoded_message += character
    return encoded_message