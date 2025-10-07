def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = {vowel: chr(ord(vowel) + 2) for vowel in vowels}
    swapped_message = message.swapcase()
    encoded_message = []
    for char in swapped_message:
        if char in vowels_replace:
            encoded_message.append(vowels_replace[char])
        else:
            encoded_message.append(char)
    return ''.join(encoded_message)