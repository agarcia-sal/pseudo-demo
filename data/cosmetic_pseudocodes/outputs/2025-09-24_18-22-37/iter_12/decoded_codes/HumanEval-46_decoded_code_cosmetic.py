from typing import List

def fib4(value_m: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]

    if 0 <= value_m < 4:
        return buffer[value_m]

    counter: int = 4
    while counter <= value_m:
        first = buffer[0]
        second = buffer[1]
        third = buffer[2]
        fourth = buffer[3]
        temp_sum = first + second + third + fourth
        buffer.append(temp_sum)
        buffer.pop(0)
        counter += 1

    return buffer[-1]