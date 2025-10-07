from typing import Union

def iscube(a: Union[int, float]) -> bool:
    a = abs(a)
    root = round(a ** (1 / 3))
    return (int(root) ** 3) == a