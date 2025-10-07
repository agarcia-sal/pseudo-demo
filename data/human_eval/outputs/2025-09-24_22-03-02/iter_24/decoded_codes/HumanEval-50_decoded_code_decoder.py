def encode_shift(s: str) -> str:
    result_list = []
    for index in range(len(s)):
        ch = s[index]
        ch_code = ord(ch)
        shifted_code = ((ch_code + 5 - ord("a")) % 26) + ord("a")
        shifted_char = chr(shifted_code)
        result_list.append(shifted_char)
    encoded_string = ""
    for index in range(len(result_list)):
        encoded_string += result_list[index]
    return encoded_string


def decode_shift(s: str) -> str:
    result_list = []
    for index in range(len(s)):
        ch = s[index]
        ch_code = ord(ch)
        shifted_code = ((ch_code - 5 - ord("a")) % 26) + ord("a")
        shifted_char = chr(shifted_code)
        result_list.append(shifted_char)
    decoded_string = ""
    for index in range(len(result_list)):
        decoded_string += result_list[index]
    return decoded_string