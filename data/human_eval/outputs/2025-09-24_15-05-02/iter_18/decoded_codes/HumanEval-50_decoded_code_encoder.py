from typing import List

def encode_shift(s: str) -> str:
    result_chars: List[str] = []
    for ch in s:
        if 'a' <= ch <= 'z':
            shifted = ((ord(ch) + 5 - ord('a')) % 26) + ord('a')
            result_chars.append(chr(shifted))
        else:
            # Preserving non-lowercase letters unchanged
            result_chars.append(ch)
    return ''.join(result_chars)

def decode_shift(s: str) -> str:
    result_chars: List[str] = []
    for ch in s:
        if 'a' <= ch <= 'z':
            shifted = ((ord(ch) - 5 - ord('a')) % 26) + ord('a')
            result_chars.append(chr(shifted))
        else:
            # Preserving non-lowercase letters unchanged
            result_chars.append(ch)
    return ''.join(result_chars)