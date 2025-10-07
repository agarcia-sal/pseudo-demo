from typing import List


def string_sequence(integer_n: int) -> str:
    buffer: List[str] = []
    index: int = 0
    while index <= integer_n:
        buffer.append(str(index))
        index += 1
    return " ".join(buffer)