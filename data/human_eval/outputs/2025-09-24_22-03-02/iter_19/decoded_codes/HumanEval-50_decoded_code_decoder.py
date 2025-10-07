def encode_shift(s: str) -> str:
    result = ""
    index = 0
    while index < len(s):
        ch = s[index]
        ch_code = ord(ch)
        base_code = ord("a")
        shifted_code = ch_code + 5 - base_code
        mod_code = shifted_code % 26
        final_code = mod_code + base_code
        shifted_char = chr(final_code)
        result += shifted_char
        index += 1
    return result

def decode_shift(s: str) -> str:
    result = ""
    index = 0
    while index < len(s):
        ch = s[index]
        ch_code = ord(ch)
        base_code = ord("a")
        shifted_code = ch_code - 5 - base_code
        mod_code = shifted_code % 26
        final_code = mod_code + base_code
        shifted_char = chr(final_code)
        result += shifted_char
        index += 1
    return result