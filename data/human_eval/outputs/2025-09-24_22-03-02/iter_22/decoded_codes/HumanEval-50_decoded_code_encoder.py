def encode_shift(s: str) -> str:
    result = []
    for i in range(len(s)):
        ch = s[i]
        shifted_code = ((ord(ch) + 5 - ord('a')) % 26) + ord('a')
        shifted_char = chr(shifted_code)
        result.append(shifted_char)
    return "".join(result)

def decode_shift(s: str) -> str:
    result = []
    for i in range(len(s)):
        ch = s[i]
        shifted_code = ((ord(ch) - 5 - ord('a')) % 26) + ord('a')
        shifted_char = chr(shifted_code)
        result.append(shifted_char)
    return "".join(result)