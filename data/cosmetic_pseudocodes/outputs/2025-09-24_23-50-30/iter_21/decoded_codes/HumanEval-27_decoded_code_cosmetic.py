from typing import List


def flip_case(text: str) -> str:
    result: List[str] = []
    index: int = 0
    while index < len(text):
        ch: str = text[index]
        if ch == ch.upper():
            if ch == ch.lower():
                result.append(ch)
            else:
                result.append(ch.lower())
        else:
            result.append(ch.upper())
        index += 1
    return ''.join(result)