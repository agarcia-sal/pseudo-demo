from typing import List

def fib4(num_param: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]
    if num_param < 4:
        return buffer[num_param]

    counter: int = 4
    while counter <= num_param:
        sum_next = buffer[0] + buffer[1] + buffer[2] + buffer[3]
        buffer.append(sum_next)
        buffer.pop(0)
        counter += 1

    return buffer[-1]