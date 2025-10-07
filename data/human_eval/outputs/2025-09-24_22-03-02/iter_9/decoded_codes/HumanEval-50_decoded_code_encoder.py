def encode_shift(input_string):
    return ''.join(chr(((ord(c) + 5 - ord('a')) % 26) + ord('a')) for c in input_string)

def decode_shift(input_string):
    return ''.join(chr(((ord(c) - 5 - ord('a')) % 26) + ord('a')) for c in input_string)