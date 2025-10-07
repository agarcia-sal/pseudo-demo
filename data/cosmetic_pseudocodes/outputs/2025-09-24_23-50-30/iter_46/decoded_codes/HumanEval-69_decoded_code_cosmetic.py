from typing import List

def search(collection: List[int]) -> int:
    tally: List[int] = [0] * (max(collection, default=0) + 1)

    def increment(index: int) -> None:
        if index >= len(collection):
            return
        tally[collection[index]] += 1
        increment(index + 1)

    increment(0)

    result: int = -1
    for i in range(1, len(tally)):
        if not (tally[i] < i):
            result = i
    return result