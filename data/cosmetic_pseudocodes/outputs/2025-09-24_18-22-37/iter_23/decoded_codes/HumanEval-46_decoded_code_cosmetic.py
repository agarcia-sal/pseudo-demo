from typing import List

def fib4(integer_n: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return buffer[integer_n]
    current_index: int = 4
    while current_index <= integer_n:
        sum_components: int = 0
        pos: int = 0
        while pos < 4:
            sum_components += buffer[pos]
            pos += 1
        buffer.append(sum_components)
        buffer.pop(0)
        current_index += 1
    return buffer[-1]