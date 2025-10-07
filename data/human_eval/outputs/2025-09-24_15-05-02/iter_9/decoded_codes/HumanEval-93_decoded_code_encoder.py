def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = {vowel: chr(ord(vowel) + 2) for vowel in vowels}
    swapped_message = message.swapcase()
    encoded_message = ''.join(vowels_replace.get(char, char) for char in swapped_message)
    return encoded_message