def encode_shift(s: str) -> str:
    result = ''
    for ch in s:
        shifted_char_code = ((ord(ch) + 5 - ord('a')) % 26) + ord('a')
        shifted_char = chr(shifted_char_code)
        result += shifted_char
    return result

def decode_shift(s: str) -> str:
    result = ''
    for ch in s:
        shifted_char_code = ((ord(ch) - 5 - ord('a')) % 26) + ord('a')
        shifted_char = chr(shifted_char_code)
        result += shifted_char
    return result