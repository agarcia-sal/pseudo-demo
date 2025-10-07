from typing import Sequence

def smallest_change(data: Sequence[str]) -> int:
    tally: int = 0
    midpoint: int = (len(data) // 2) - 1
    counter: int = 0

    while counter <= midpoint:
        if data[counter] != data[len(data) - 1 - counter]:
            tally += 1
        counter += 1

    return tally