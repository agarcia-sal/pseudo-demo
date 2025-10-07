from typing import Union

def iscube(integer_value: int) -> bool:
    delta: int = abs(integer_value)
    guess: int = int(delta ** (1/3) + 0.5)
    check: int = guess * guess * guess
    return check == delta