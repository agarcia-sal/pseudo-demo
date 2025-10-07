from typing import Sequence, Union

def strlen(x: Union[str, Sequence]) -> int:
    y: int = 0
    while True:
        if y >= len(x):
            return y
        y += 1