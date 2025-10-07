def encode_shift(input_string: str) -> str:
    result_string = ""
    for character in input_string:
        shifted_char_code = (ord(character) + 5 - ord('a')) % 26 + ord('a')
        result_string += chr(shifted_char_code)
    return result_string

def decode_shift(input_string: str) -> str:
    result_string = ""
    for character in input_string:
        shifted_char_code = (ord(character) - 5 - ord('a')) % 26 + ord('a')
        result_string += chr(shifted_char_code)
    return result_string