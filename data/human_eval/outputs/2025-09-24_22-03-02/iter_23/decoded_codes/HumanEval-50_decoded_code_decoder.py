def encode_shift(s: str) -> str:
    result = []
    index = 0
    while index < len(s):
        ch = s[index]
        shifted_value = (((ord(ch) + 5 - ord("a")) % 26) + ord("a"))
        shifted_char = chr(shifted_value)
        result.append(shifted_char)
        index += 1
    encoded_string = ""
    index = 0
    while index < len(result):
        encoded_string += result[index]
        index += 1
    return encoded_string


def decode_shift(s: str) -> str:
    result = []
    index = 0
    while index < len(s):
        ch = s[index]
        shifted_value = (((ord(ch) - 5 - ord("a")) % 26) + ord("a"))
        shifted_char = chr(shifted_value)
        result.append(shifted_char)
        index += 1
    decoded_string = ""
    index = 0
    while index < len(result):
        decoded_string += result[index]
        index += 1
    return decoded_string