from typing import List

def fib4(integer_n: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return buffer[integer_n]

    index: int = 4
    while index <= integer_n:
        sum_value: int = buffer[0] + buffer[1] + buffer[2] + buffer[3]
        buffer = buffer[1:] + [sum_value]
        index += 1

    return buffer[3]