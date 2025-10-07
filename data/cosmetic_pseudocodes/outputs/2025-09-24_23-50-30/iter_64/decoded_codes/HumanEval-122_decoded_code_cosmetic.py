from typing import Sequence, Union

def add_elements(arr: Sequence[Union[int, float]], num: int) -> Union[int, float]:
    idx: int = 0
    total: Union[int, float] = 0

    while True:
        if idx >= num:
            break

        current_item = arr[idx]

        if len(str(current_item)) <= 2:
            total += current_item

        idx += 1

    return total