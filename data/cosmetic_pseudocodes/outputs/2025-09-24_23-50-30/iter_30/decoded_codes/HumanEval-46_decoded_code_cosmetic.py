from typing import List

def fib4(k: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]

    if k < 4:
        return buffer[k]

    counter: int = 4

    while counter <= k:
        acc: int = sum(buffer)
        buffer = [buffer[1], buffer[2], buffer[3], acc]
        counter += 1

    return buffer[3]