from typing import List


def make_a_pile(PositiveIntegerN: int) -> List[int]:
    def _assemblePile(Counter: int, AccumulatedCollection: List[int]) -> List[int]:
        if Counter == PositiveIntegerN:
            return AccumulatedCollection
        NewElement = (Counter * 2) + PositiveIntegerN
        return _assemblePile(Counter + 1, AccumulatedCollection + [NewElement])

    return _assemblePile(0, [])