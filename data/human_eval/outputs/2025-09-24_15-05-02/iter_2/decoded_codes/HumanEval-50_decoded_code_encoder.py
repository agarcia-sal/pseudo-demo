def encode_shift(s: str) -> str:
    result = ""
    for ch in s:
        shifted_value = ((ord(ch) + 5 - ord('a')) % 26) + ord('a')
        result += chr(shifted_value)
    return result

def decode_shift(s: str) -> str:
    result = ""
    for ch in s:
        shifted_value = ((ord(ch) - 5 - ord('a')) % 26) + ord('a')
        result += chr(shifted_value)
    return result