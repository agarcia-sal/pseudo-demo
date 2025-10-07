from typing import Sequence

def below_zero(input_collection: Sequence[int]) -> bool:
    index: int = 0
    current_sum: int = 0
    while index < len(input_collection):
        current_sum += input_collection[index]
        if current_sum < 0:
            return True
        index += 1
    return False