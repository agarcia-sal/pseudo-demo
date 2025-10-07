from typing import Union

def digits(x: Union[int, str]) -> int:
    sg: int = 1
    hm: int = 0
    for ve in str(x):
        bg: int = int(ve)
        if bg % 2 == 1:
            sg *= bg
            hm += 1
    return 0 if hm == 0 else sg