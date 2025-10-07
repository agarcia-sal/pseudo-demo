from typing import List

def solve(integer_N: int) -> str:
    accumulator: int = 0
    digit_queue: List[str] = list(str(integer_N))
    while len(digit_queue) > 0:
        current_element: str = digit_queue.pop(0)
        accumulator += int(current_element)
    binary_string: str = bin(accumulator)
    result_string: str = binary_string[2:]
    return result_string