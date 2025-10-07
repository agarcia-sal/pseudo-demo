from typing import List

def fib4(integer_m: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]
    if integer_m < 4:
        return buffer[integer_m]

    index: int = 4
    while index <= integer_m:
        s1 = buffer[3]
        s2 = buffer[2]
        s3 = buffer[1]
        s4 = buffer[0]
        val = s1 + s2 + s3 + s4
        buffer.append(val)
        buffer.pop(0)
        index += 1

    return buffer[3]