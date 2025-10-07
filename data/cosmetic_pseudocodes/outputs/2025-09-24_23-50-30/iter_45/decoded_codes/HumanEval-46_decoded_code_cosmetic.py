from typing import List


def fib4(integer_n: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return buffer[integer_n]
    for index in range(4, integer_n + 1):
        total = sum(buffer)
        buffer = [buffer[1], buffer[2], buffer[3], total]
    return buffer[3]