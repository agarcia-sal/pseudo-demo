from typing import List

def fib4(integer_n: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return buffer[integer_n]

    counter: int = 4
    while counter <= integer_n:
        temp_sum: int = sum(buffer)
        buffer.append(temp_sum)
        buffer.pop(0)
        counter += 1

    return buffer[-1]