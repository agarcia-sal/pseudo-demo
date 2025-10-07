from typing import Union


def digits(m: Union[int, str]) -> int:
    accumulation: int = 1
    tally: int = 0
    for element in str(m):
        value = int(element)
        if value % 2 != 0:
            accumulation *= value
            tally += 1
    if tally == 0:
        return 0
    return accumulation