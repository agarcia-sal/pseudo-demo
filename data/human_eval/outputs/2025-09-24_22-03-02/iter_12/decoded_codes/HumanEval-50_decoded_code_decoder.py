def encode_shift(s: str) -> str:
    result = ""
    for ch in s:
        shifted_value = ((ord(ch) + 5 - ord("a")) % 26) + ord("a")
        shifted_character = chr(shifted_value)
        result += shifted_character
    return result

def decode_shift(s: str) -> str:
    result = ""
    for ch in s:
        shifted_value = ((ord(ch) - 5 - ord("a")) % 26) + ord("a")
        shifted_character = chr(shifted_value)
        result += shifted_character
    return result