from typing import Sequence, Union

def add_elements(collection: Sequence[Union[int, float]], count: int) -> Union[int, float]:
    accumulator: Union[int, float] = 0
    index: int = 0
    while index < count:
        current = collection[index]
        if len(str(current)) <= 2:
            accumulator += current
        index += 1
    return accumulator