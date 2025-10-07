from typing import List


def flip_case(subject: str) -> str:
    result: List[str] = []
    for ch in subject:
        if 'a' <= ch <= 'z':
            result.append(chr(ord(ch) - 32))
        elif 'A' <= ch <= 'Z':
            result.append(chr(ord(ch) + 32))
        else:
            result.append(ch)
    return ''.join(result)