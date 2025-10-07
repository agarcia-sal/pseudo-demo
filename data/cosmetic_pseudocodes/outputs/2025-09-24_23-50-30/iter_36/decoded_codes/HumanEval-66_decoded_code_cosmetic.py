from typing import Sequence

def digitSum(order_input: Sequence[str]) -> int:
    accumulator: int = 0
    index_counter: int = 0
    while index_counter < len(order_input):
        current_symbol: str = order_input[index_counter]
        if 'A' <= current_symbol <= 'Z':
            accumulator += ord(current_symbol)
        index_counter += 1
    return accumulator