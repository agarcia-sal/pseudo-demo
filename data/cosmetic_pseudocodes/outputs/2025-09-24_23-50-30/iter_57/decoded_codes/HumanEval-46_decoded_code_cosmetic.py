from typing import List


def fib4(integer_n: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return buffer[integer_n]

    index = 4
    while index <= integer_n:
        new_entry = sum(buffer)
        buffer.append(new_entry)
        buffer.pop(0)
        index += 1
    return buffer[3]