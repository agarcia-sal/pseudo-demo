from typing import List


def fib4(integer_n: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return buffer[integer_n]

    idx: int = 4
    while idx <= integer_n:
        a, b, c, d = buffer[0], buffer[1], buffer[2], buffer[3]
        sum_value = a + b + c + d
        buffer.append(sum_value)
        buffer.pop(0)
        idx += 1

    return buffer[-1]