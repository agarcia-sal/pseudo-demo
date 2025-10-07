from typing import List


def fizz_buzz(k: int) -> int:
    buffer: str = ""
    S: List[int] = []

    def loop1(idx: int) -> None:
        if idx < k:
            if idx % 11 == 0 or idx % 13 == 0:
                S.append(idx)
            loop1(idx + 1)

    loop1(0)

    while True:
        for e in S:
            buffer += str(e)
        break

    accumulator: int = 0
    cursor: int = 0
    while cursor < len(buffer):
        if buffer[cursor] == '7':
            accumulator += 1
        cursor += 1

    return accumulator