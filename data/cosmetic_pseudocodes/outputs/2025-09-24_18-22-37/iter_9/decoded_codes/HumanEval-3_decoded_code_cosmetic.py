from typing import Sequence


def below_zero(collection_ops: Sequence[int]) -> bool:
    accumulator: int = 0
    for idx in range(len(collection_ops)):
        current_item: int = collection_ops[idx]
        temp_sum: int = accumulator + current_item
        accumulator = temp_sum
        if not (accumulator >= 0):
            return True
    return False