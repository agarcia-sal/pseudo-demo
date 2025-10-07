from typing import Sequence, Union

def add_elements(collection: Sequence[Union[int, float]], count: int) -> Union[int, float]:
    total_sum: Union[int, float] = 0
    cursor: int = 0
    while cursor < count:
        item = collection[cursor]
        str_length = len(str(item))
        if not (str_length > 2):
            total_sum += item
        cursor += 1
    return total_sum