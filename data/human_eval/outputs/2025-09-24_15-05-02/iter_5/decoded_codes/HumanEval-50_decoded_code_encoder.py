def encode_shift(s: str) -> str:
    encoded_characters = []
    for character in s:
        shifted_value = (ord(character) + 5 - ord('a')) % 26
        encoded_character = chr(shifted_value + ord('a'))
        encoded_characters.append(encoded_character)
    return ''.join(encoded_characters)

def decode_shift(s: str) -> str:
    decoded_characters = []
    for character in s:
        shifted_value = (ord(character) - 5 - ord('a')) % 26
        decoded_character = chr(shifted_value + ord('a'))
        decoded_characters.append(decoded_character)
    return ''.join(decoded_characters)