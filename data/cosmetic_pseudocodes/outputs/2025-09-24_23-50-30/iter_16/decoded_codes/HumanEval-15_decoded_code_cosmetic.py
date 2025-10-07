from typing import List

def string_sequence(integer_n: int) -> str:
    index: int = 0
    segments: List[str] = []
    while index <= integer_n:
        segments.append(str(index))
        index += 1
    return " ".join(segments)