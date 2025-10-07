from typing import Union

def how_many_times(f1: Union[str, list], f2: Union[str, list]) -> int:
    f3: int = 0
    f4: int = len(f1) - len(f2)
    f5: int = 0
    while f5 <= f4:
        if f1[f5 : f5 + len(f2)] == f2:
            f3 += 1
        f5 += 1
    return f3