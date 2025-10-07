def encode_shift(s: str):
    result = []
    for ch in s:
        shifted_value = (ord(ch) + 5 - ord("a")) % 26 + ord("a")
        shifted_char = chr(shifted_value)
        result.append(shifted_char)
    encoded_string = ""
    for character in result:
        encoded_string += character
    return encoded_string

def decode_shift(s: str):
    result = []
    for ch in s:
        shifted_value = (ord(ch) - 5 - ord("a")) % 26 + ord("a")
        shifted_char = chr(shifted_value)
        result.append(shifted_char)
    decoded_string = ""
    for character in result:
        decoded_string += character
    return decoded_string