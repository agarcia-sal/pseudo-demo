from typing import List, Optional

def rolling_max(array_of_values: List[int]) -> List[int]:
    accumulator: Optional[int] = None
    collection: List[int] = []

    def iterate(index: int) -> None:
        if index >= len(array_of_values):
            return
        nonlocal accumulator
        if accumulator is None:
            accumulator = array_of_values[index]
        else:
            if accumulator < array_of_values[index]:
                accumulator = array_of_values[index]
        collection.append(accumulator)
        iterate(index + 1)

    iterate(0)
    return collection