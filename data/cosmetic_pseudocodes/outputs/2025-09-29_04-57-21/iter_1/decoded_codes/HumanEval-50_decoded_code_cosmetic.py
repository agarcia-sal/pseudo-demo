def encode_shift(input_string: str) -> str:
    output: str = ""
    for ch in input_string:
        code = ord(ch) - ord("a")
        shifted = (code + 5) % 26
        new_char = chr(shifted + ord("a"))
        output += new_char
    return output


def decode_shift(input_string: str) -> str:
    result: str = ""
    for index in range(len(input_string)):
        val = ord(input_string[index]) - ord("a")
        adjusted = (val - 5) % 26
        decoded_char = chr(adjusted + ord("a"))
        result += decoded_char
    return result