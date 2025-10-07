def encode_shift(s: str) -> str:
    result = []
    length = len(s)
    index = 0
    while index < length:
        ch = s[index]
        char_code = ord(ch)
        shifted_code = (char_code + 5 - ord("a")) % 26 + ord("a")
        shifted_char = chr(shifted_code)
        result.append(shifted_char)
        index += 1
    encoded_string = ""
    j = 0
    result_length = len(result)
    while j < result_length:
        encoded_string += result[j]
        j += 1
    return encoded_string

def decode_shift(s: str) -> str:
    result = []
    length = len(s)
    index = 0
    while index < length:
        ch = s[index]
        char_code = ord(ch)
        shifted_code = (char_code - 5 - ord("a")) % 26 + ord("a")
        shifted_char = chr(shifted_code)
        result.append(shifted_char)
        index += 1
    decoded_string = ""
    j = 0
    result_length = len(result)
    while j < result_length:
        decoded_string += result[j]
        j += 1
    return decoded_string