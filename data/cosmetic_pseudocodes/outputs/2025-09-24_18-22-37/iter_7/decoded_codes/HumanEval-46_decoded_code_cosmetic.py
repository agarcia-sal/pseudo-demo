from typing import List

def fib4(count_input: int) -> int:
    buffer: List[int] = [0, 0, 2, 0]
    if count_input < 4:
        return buffer[count_input]

    index_counter: int = 4
    while index_counter <= count_input:
        a, b, c, d = buffer
        aggregated_sum = a + b + c + d

        buffer.append(aggregated_sum)
        buffer.pop(0)

        index_counter += 1

    return buffer[-1]