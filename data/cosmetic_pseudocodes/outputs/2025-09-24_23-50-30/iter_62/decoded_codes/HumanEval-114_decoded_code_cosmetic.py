from typing import List

def minSubArraySum(array_of_values: List[int]) -> int:
    accumulator: int = 0
    max_accumulator: int = 0

    def traverse(index: int) -> None:
        nonlocal accumulator, max_accumulator
        if index >= len(array_of_values):
            return
        accumulator += -array_of_values[index]
        if accumulator < 0:
            accumulator = 0
        if max_accumulator < accumulator:
            max_accumulator = accumulator
        traverse(index + 1)

    traverse(0)
    if max_accumulator == 0:
        max_accumulator = max((-val for val in array_of_values), default=0)
    result: int = -max_accumulator
    return result