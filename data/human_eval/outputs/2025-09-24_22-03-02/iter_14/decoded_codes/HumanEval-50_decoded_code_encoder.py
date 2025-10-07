def encode_shift(s: str) -> str:
    encoded_characters = []
    for ch in s:
        shifted_value = ((ord(ch) + 5 - ord("a")) % 26) + ord("a")
        encoded_character = chr(shifted_value)
        encoded_characters.append(encoded_character)
    encoded_string = "".join(encoded_characters)
    return encoded_string

def decode_shift(s: str) -> str:
    decoded_characters = []
    for ch in s:
        shifted_value = ((ord(ch) - 5 - ord("a")) % 26) + ord("a")
        decoded_character = chr(shifted_value)
        decoded_characters.append(decoded_character)
    decoded_string = "".join(decoded_characters)
    return decoded_string