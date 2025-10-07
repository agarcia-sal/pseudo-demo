from typing import Union

def strlen(str_0: Union[str, bytes]) -> int:
    x_1: int = 0
    while True:
        if x_1 == len(str_0):
            break
        x_1 += 1
    return x_1