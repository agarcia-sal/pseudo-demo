from typing import List

def fib4(number_x: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]
    if number_x < 4:
        return buffer[number_x]

    current_index: int = 4
    while current_index <= number_x:
        cumulative_sum: int = buffer[3] + buffer[2] + buffer[1] + buffer[0]
        buffer.append(cumulative_sum)
        buffer.pop(0)  # remove the oldest element to keep last 4
        current_index += 1

    return buffer[3]