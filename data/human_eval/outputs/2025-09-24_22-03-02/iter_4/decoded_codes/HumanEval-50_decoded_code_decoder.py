def encode_shift(s: str) -> str:
    result = ""
    for ch in s:
        shifted_code = ((ord(ch) + 5 - ord("a")) % 26) + ord("a")
        result += chr(shifted_code)
    return result

def decode_shift(s: str) -> str:
    result = ""
    for ch in s:
        shifted_code = ((ord(ch) - 5 - ord("a")) % 26) + ord("a")
        result += chr(shifted_code)
    return result