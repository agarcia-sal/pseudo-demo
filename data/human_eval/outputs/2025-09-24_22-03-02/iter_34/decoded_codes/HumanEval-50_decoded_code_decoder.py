def encode_shift(s: str) -> str:
    result = []
    base_code = ord("a")
    for i in range(len(s)):
        ch = s[i]
        ch_code = ord(ch)
        shifted_value = ch_code + 5 - base_code
        modulo_value = shifted_value % 26
        new_char_code = modulo_value + base_code
        new_char = chr(new_char_code)
        result.append(new_char)
    joined_string = ""
    for j in range(len(result)):
        joined_string += result[j]
    return joined_string

def decode_shift(s: str) -> str:
    result = []
    base_code = ord("a")
    for i in range(len(s)):
        ch = s[i]
        ch_code = ord(ch)
        shifted_value = ch_code - 5 - base_code
        modulo_value = shifted_value % 26
        new_char_code = modulo_value + base_code
        new_char = chr(new_char_code)
        result.append(new_char)
    joined_string = ""
    for j in range(len(result)):
        joined_string += result[j]
    return joined_string