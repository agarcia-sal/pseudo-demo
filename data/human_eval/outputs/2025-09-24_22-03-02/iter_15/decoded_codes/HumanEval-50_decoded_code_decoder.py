def encode_shift(s: str) -> str:
    shifted_characters = []
    for ch in s:
        shifted_value = (ord(ch) + 5 - ord("a")) % 26 + ord("a")
        shifted_character = chr(shifted_value)
        shifted_characters.append(shifted_character)
    encoded_string = "".join(shifted_characters)
    return encoded_string

def decode_shift(s: str) -> str:
    shifted_characters = []
    for ch in s:
        shifted_value = (ord(ch) - 5 - ord("a")) % 26 + ord("a")
        shifted_character = chr(shifted_value)
        shifted_characters.append(shifted_character)
    decoded_string = "".join(shifted_characters)
    return decoded_string