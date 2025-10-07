from typing import List


def fib4(integer_n: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]
    if integer_n >= 4:
        index: int = 4
        while index <= integer_n:
            temp: int = sum(buffer)
            buffer.pop(0)
            buffer.append(temp)
            index += 1
        return buffer[3]
    return buffer[integer_n]