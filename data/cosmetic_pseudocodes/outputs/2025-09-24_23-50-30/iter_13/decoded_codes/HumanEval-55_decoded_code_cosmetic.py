from typing import List


def fib(integer_n: int) -> int:
    if integer_n == 0:
        return 0
    if integer_n == 1:
        return 1
    sequence_values: List[int] = [0, 1]
    index_counter: int = 2
    while index_counter <= integer_n:
        next_value = sequence_values[index_counter - 2] + sequence_values[index_counter - 1]
        sequence_values.append(next_value)
        index_counter += 1
    return sequence_values[integer_n]