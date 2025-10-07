def encode_shift(s: str) -> str:
    encoded_chars = []
    length_to_process = len(s)
    index = 0
    while index < length_to_process:
        ch = s[index]
        char_code = ord(ch)
        base_code = ord("a")
        shifted_code = ((char_code + 5 - base_code) % 26) + base_code
        shifted_char = chr(shifted_code)
        encoded_chars.append(shifted_char)
        index += 1
    result = ""
    index = 0
    length_to_join = len(encoded_chars)
    while index < length_to_join:
        result += encoded_chars[index]
        index += 1
    return result

def decode_shift(s: str) -> str:
    decoded_chars = []
    length_to_process = len(s)
    index = 0
    while index < length_to_process:
        ch = s[index]
        char_code = ord(ch)
        base_code = ord("a")
        shifted_code = ((char_code - 5 - base_code) % 26) + base_code
        shifted_char = chr(shifted_code)
        decoded_chars.append(shifted_char)
        index += 1
    result = ""
    index = 0
    length_to_join = len(decoded_chars)
    while index < length_to_join:
        result += decoded_chars[index]
        index += 1
    return result