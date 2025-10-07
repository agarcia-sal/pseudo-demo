from typing import Union

def iscube(num: Union[int, float]) -> bool:
    val: float = -num if num < 0 else num
    guess: int = round(val ** (1/3))
    return guess * guess * guess == val