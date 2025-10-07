from typing import List

def encode_shift(string: str) -> str:
    """
    Encodes the input string by shifting each lowercase letter 5 positions forward in the alphabet,
    wrapping around using modulo 26. Assumes input consists of lowercase letters 'a'-'z'.
    """
    a_ord = ord('a')
    result_chars: List[str] = []
    for char in string:
        shifted_code = (ord(char) + 5 - a_ord) % 26 + a_ord
        result_chars.append(chr(shifted_code))
    return ''.join(result_chars)

def decode_shift(string: str) -> str:
    """
    Decodes the input string by shifting each lowercase letter 5 positions backward in the alphabet,
    wrapping around using modulo 26. Assumes input consists of lowercase letters 'a'-'z'.
    """
    a_ord = ord('a')
    result_chars: List[str] = []
    for char in string:
        shifted_code = (ord(char) - 5 - a_ord) % 26 + a_ord
        result_chars.append(chr(shifted_code))
    return ''.join(result_chars)