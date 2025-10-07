def encode_shift(s):
    return ''.join(chr(((ord(c) + 5 - ord('a')) % 26) + ord('a')) for c in s)

def decode_shift(s):
    return ''.join(chr(((ord(c) - 5 - ord('a')) % 26) + ord('a')) for c in s)