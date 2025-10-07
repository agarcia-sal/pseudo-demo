from typing import Union


def iscube(number: Union[int, float]) -> bool:
    positive_equiv: float = -number if number < 0 else number
    guess: int = int(pow(positive_equiv, 1/3) + 0.5)
    cube_calc: int = guess * guess * guess
    return cube_calc == positive_equiv