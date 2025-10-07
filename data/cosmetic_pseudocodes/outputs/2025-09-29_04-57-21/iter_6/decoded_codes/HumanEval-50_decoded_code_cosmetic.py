from typing import List

def encode_shift(input_string: str) -> str:
    encoded_chars: List[str] = []
    a_ord = ord('a')
    for each_letter in input_string:
        ascii_num = ord(each_letter)
        adjusted_num = ((ascii_num + 5) - a_ord) % 26
        shifted_ascii = adjusted_num + a_ord
        encoded_chars.append(chr(shifted_ascii))
    return ''.join(encoded_chars)

def decode_shift(input_string: str) -> str:
    decoded_chars: List[str] = []
    a_ord = ord('a')
    for each_letter in input_string:
        ascii_num = ord(each_letter)
        adjusted_num = ((ascii_num - 5) - a_ord) % 26
        shifted_ascii = adjusted_num + a_ord
        decoded_chars.append(chr(shifted_ascii))
    return ''.join(decoded_chars)