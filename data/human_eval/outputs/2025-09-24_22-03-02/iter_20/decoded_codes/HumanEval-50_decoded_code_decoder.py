def encode_shift(s: str) -> str:
    result = []
    for ch in s:
        shifted_value = ((ord(ch) + 5 - ord("a")) % 26) + ord("a")
        shifted_char = chr(shifted_value)
        result.append(shifted_char)
    encoded_string = ""
    for ch in result:
        encoded_string += ch
    return encoded_string


def decode_shift(s: str) -> str:
    result = []
    for ch in s:
        shifted_value = ((ord(ch) - 5 - ord("a")) % 26) + ord("a")
        shifted_char = chr(shifted_value)
        result.append(shifted_char)
    decoded_string = ""
    for ch in result:
        decoded_string += ch
    return decoded_string