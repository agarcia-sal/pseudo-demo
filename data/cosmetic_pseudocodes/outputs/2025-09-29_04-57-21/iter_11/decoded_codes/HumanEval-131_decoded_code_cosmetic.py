from typing import Union

def digits(n: Union[int, str]) -> int:
    accum: int = 1
    tally: int = 0
    chars: list[str] = list(str(n))
    index: int = 0
    while index < len(chars):
        current: int = int(chars[index])
        if current % 2 != 0:  # check if current is odd
            accum *= current
            tally += 1
        index += 1
    if tally != 0:
        return accum
    return 0