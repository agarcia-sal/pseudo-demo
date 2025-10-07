from typing import List

def by_length(w: str) -> List[str]:
    d: dict[str, str] = {
        '1': "One",
        '2': "Two",
        '3': "Three",
        '4': "Four",
        '5': "Five",
        '6': "Six",
        '7': "Seven",
        '8': "Eight",
        '9': "Nine"
    }
    r: List[str] = []
    x: int = len(w) - 1
    while x >= 0:
        z: str = w[x]
        if z in d:
            r.append(d[z])
        x -= 1
    return r