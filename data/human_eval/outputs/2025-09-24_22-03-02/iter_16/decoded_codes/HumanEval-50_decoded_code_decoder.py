def encode_shift(s: str) -> str:
    result_characters = []
    for ch in s:
        shifted_value = ((ord(ch) + 5 - ord("a")) % 26) + ord("a")
        shifted_character = chr(shifted_value)
        result_characters.append(shifted_character)
    encoded_string = "".join(result_characters)
    return encoded_string

def decode_shift(s: str) -> str:
    result_characters = []
    for ch in s:
        shifted_value = ((ord(ch) - 5 - ord("a")) % 26) + ord("a")
        shifted_character = chr(shifted_value)
        result_characters.append(shifted_character)
    decoded_string = "".join(result_characters)
    return decoded_string