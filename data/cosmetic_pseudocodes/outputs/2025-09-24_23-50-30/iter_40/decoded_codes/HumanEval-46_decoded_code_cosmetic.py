from typing import List

def fib4(integer_n: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return buffer[integer_n]

    counter: int = 4
    while counter <= integer_n:
        temp = sum(buffer)
        buffer[0], buffer[1], buffer[2], buffer[3] = buffer[1], buffer[2], buffer[3], temp
        counter += 1

    return buffer[3]