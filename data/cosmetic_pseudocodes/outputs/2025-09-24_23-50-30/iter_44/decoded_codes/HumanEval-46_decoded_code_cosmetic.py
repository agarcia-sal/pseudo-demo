from typing import List

def fib4(index_arg: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]
    if index_arg < 4:
        return buffer[index_arg]
    counter: int = 4
    while counter <= index_arg:
        temp_sum: int = sum(buffer)
        buffer = buffer[1:] + [temp_sum]
        counter += 1
    return buffer[3]