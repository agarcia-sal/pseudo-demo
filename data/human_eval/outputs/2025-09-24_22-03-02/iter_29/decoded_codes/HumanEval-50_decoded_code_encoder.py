def encode_shift(s: str) -> str:
    result = []
    for i in range(len(s)):
        ch = s[i]
        shifted_value = ((ord(ch) + 5 - ord('a')) % 26) + ord('a')
        shifted_char = chr(shifted_value)
        result.append(shifted_char)
    encoded_string = ''
    for i in range(len(result)):
        encoded_string += result[i]
    return encoded_string

def decode_shift(s: str) -> str:
    result = []
    for i in range(len(s)):
        ch = s[i]
        shifted_value = ((ord(ch) - 5 - ord('a')) % 26) + ord('a')
        shifted_char = chr(shifted_value)
        result.append(shifted_char)
    decoded_string = ''
    for i in range(len(result)):
        decoded_string += result[i]
    return decoded_string