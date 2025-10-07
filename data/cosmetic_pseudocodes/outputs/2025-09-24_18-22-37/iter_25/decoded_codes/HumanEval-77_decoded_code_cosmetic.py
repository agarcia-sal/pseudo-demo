from typing import Union

def iscube(w: Union[int, float]) -> bool:
    u: Union[int, float] = w
    v: Union[int, float] = -u if u < 0 else u

    a: Union[int, float] = v
    b: int = 3
    c: int = 1
    d: float = c / b
    e: float = a ** d
    f: int = round(e)
    g: int = f ** b

    return g == v