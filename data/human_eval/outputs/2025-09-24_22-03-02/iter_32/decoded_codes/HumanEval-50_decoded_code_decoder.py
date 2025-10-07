def encode_shift(s: str) -> str:
    result = []
    length = len(s)
    index = 0
    while index < length:
        ch = s[index]
        ch_code = ord(ch)
        a_code = ord("a")
        shifted_code = ch_code + 5 - a_code
        mod_code = shifted_code % 26
        final_code = mod_code + a_code
        encoded_char = chr(final_code)
        result.append(encoded_char)
        index += 1
    encoded_string = ""
    result_length = len(result)
    result_index = 0
    while result_index < result_length:
        encoded_string += result[result_index]
        result_index += 1
    return encoded_string


def decode_shift(s: str) -> str:
    result = []
    length = len(s)
    index = 0
    while index < length:
        ch = s[index]
        ch_code = ord(ch)
        a_code = ord("a")
        shifted_code = ch_code - 5 - a_code
        mod_code = shifted_code % 26
        final_code = mod_code + a_code
        decoded_char = chr(final_code)
        result.append(decoded_char)
        index += 1
    decoded_string = ""
    result_length = len(result)
    result_index = 0
    while result_index < result_length:
        decoded_string += result[result_index]
        result_index += 1
    return decoded_string