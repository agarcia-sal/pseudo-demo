def encode_shift(s: str) -> str:
    result = []
    length = len(s)
    index = 0
    while index < length:
        ch = s[index]
        original_code = ord(ch)
        a_code = ord("a")
        shifted_code = original_code + 5 - a_code
        mod_code = shifted_code % 26
        final_code = mod_code + a_code
        shifted_character = chr(final_code)
        result.append(shifted_character)
        index += 1
    encoded_string = "".join(result)
    return encoded_string

def decode_shift(s: str) -> str:
    result = []
    length = len(s)
    index = 0
    while index < length:
        ch = s[index]
        original_code = ord(ch)
        a_code = ord("a")
        shifted_code = original_code - 5 - a_code
        mod_code = shifted_code % 26
        final_code = mod_code + a_code
        shifted_character = chr(final_code)
        result.append(shifted_character)
        index += 1
    decoded_string = "".join(result)
    return decoded_string