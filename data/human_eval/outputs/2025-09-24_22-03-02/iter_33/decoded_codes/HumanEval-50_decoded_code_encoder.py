def encode_shift(s: str) -> str:
    result = []
    length = len(s)
    index = 0
    while index < length:
        ch = s[index]
        ch_ord = ord(ch)
        base = ord("a")
        shifted_value = ch_ord + 5 - base
        modulo_value = shifted_value % 26
        final_value = modulo_value + base
        shifted_char = chr(final_value)
        result.append(shifted_char)
        index += 1
    encoded_string = ""
    j = 0
    result_length = len(result)
    while j < result_length:
        encoded_string += result[j]
        j += 1
    return encoded_string

def decode_shift(s: str) -> str:
    result = []
    length = len(s)
    index = 0
    while index < length:
        ch = s[index]
        ch_ord = ord(ch)
        base = ord("a")
        shifted_value = ch_ord - 5 - base
        modulo_value = shifted_value % 26
        final_value = modulo_value + base
        shifted_char = chr(final_value)
        result.append(shifted_char)
        index += 1
    decoded_string = ""
    j = 0
    result_length = len(result)
    while j < result_length:
        decoded_string += result[j]
        j += 1
    return decoded_string