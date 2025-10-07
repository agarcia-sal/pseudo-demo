def encode_shift(s: str) -> str:
    result = ""
    index = 0
    while index < len(s):
        ch = s[index]
        code = ord(ch)
        base = ord("a")
        shifted_code = ((code + 5 - base) % 26) + base
        shifted_char = chr(shifted_code)
        result += shifted_char
        index += 1
    return result

def decode_shift(s: str) -> str:
    result = ""
    index = 0
    while index < len(s):
        ch = s[index]
        code = ord(ch)
        base = ord("a")
        shifted_code = ((code - 5 - base) % 26) + base
        shifted_char = chr(shifted_code)
        result += shifted_char
        index += 1
    return result