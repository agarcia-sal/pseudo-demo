from typing import List


def flip_case(keyword: str) -> str:
    index: int = 0
    result: List[str] = []
    while index < len(keyword):
        cipher: str = keyword[index]
        if 'a' <= cipher <= 'z':
            result.append(cipher.upper())
        elif 'A' <= cipher <= 'Z':
            result.append(cipher.lower())
        else:
            result.append(cipher)
        index += 1
    return ''.join(result)