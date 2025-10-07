def encode_shift(s: str) -> str:
    encoded_string = ""
    for character in s:
        shifted_character_code = ((ord(character) + 5 - ord("a")) % 26) + ord("a")
        shifted_character = chr(shifted_character_code)
        encoded_string += shifted_character
    return encoded_string

def decode_shift(s: str) -> str:
    decoded_string = ""
    for character in s:
        shifted_character_code = ((ord(character) - 5 - ord("a")) % 26) + ord("a")
        shifted_character = chr(shifted_character_code)
        decoded_string += shifted_character
    return decoded_string