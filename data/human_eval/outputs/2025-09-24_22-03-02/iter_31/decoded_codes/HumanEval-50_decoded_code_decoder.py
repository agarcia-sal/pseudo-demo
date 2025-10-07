def encode_shift(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        ch = s[i]
        original_value = ord(ch)
        shifted_value = original_value + 5 - ord("a")
        wrapped_value = shifted_value % 26
        new_char_code = wrapped_value + ord("a")
        new_char = chr(new_char_code)
        result.append(new_char)
        i += 1
    encoded_string = ""
    j = 0
    while j < len(result):
        encoded_string += result[j]
        j += 1
    return encoded_string

def decode_shift(s: str) -> str:
    result = []
    i = 0
    while i < len(s):
        ch = s[i]
        original_value = ord(ch)
        shifted_value = original_value - 5 - ord("a")
        wrapped_value = shifted_value % 26
        new_char_code = wrapped_value + ord("a")
        new_char = chr(new_char_code)
        result.append(new_char)
        i += 1
    decoded_string = ""
    j = 0
    while j < len(result):
        decoded_string += result[j]
        j += 1
    return decoded_string