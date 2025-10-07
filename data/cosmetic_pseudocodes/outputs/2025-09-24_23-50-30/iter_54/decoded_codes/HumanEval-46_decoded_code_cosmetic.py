from typing import List


def fib4(integer_n: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return buffer[integer_n]

    index: int = 4
    while index <= integer_n:
        candidate: int = sum(buffer)
        buffer.append(candidate)
        del buffer[0]
        index += 1

    return buffer[-1]