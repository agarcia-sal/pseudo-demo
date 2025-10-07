def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {v: chr(ord(v) + 2) for v in vowels}
    swapped_message = message.swapcase()
    result_characters = [
        vowels_replace[c] if c in vowels else c for c in swapped_message
    ]
    encoded_message = ''.join(result_characters)
    return encoded_message