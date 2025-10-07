from typing import List


def fib4(count: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]

    if count < 4:
        return buffer[count]

    index: int = 4
    while index <= count:
        a, b, c, d = buffer
        sum_of_last_four: int = a + b + c + d

        buffer.append(sum_of_last_four)
        buffer.pop(0)

        index += 1

    return buffer[-1]