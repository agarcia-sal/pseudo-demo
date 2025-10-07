def encode_shift(s: str) -> str:
    result = []
    for ch in s:
        shifted_value = ((ord(ch) + 5 - ord("a")) % 26) + ord("a")
        shifted_char = chr(shifted_value)
        result.append(shifted_char)
    return ''.join(result)

def decode_shift(s: str) -> str:
    result = []
    for ch in s:
        shifted_value = ((ord(ch) - 5 - ord("a")) % 26) + ord("a")
        shifted_char = chr(shifted_value)
        result.append(shifted_char)
    return ''.join(result)