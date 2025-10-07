from typing import List

def fib4(integer_n: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return buffer[integer_n]

    idx: int = 4
    while idx <= integer_n:
        new_val: int = sum(buffer)
        buffer.append(new_val)
        del buffer[0]
        idx += 1

    return buffer[3]