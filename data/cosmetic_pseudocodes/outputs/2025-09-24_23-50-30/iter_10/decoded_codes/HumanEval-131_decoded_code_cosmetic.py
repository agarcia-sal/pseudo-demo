from typing import Union

def digits(n: Union[int, str]) -> int:
    acc: int = 1
    tally: int = 0
    for char in str(n):
        val: int = int(char)
        if val % 2 == 1:
            acc *= val
            tally += 1
    return 0 if tally == 0 else acc