from typing import List, Sequence


def is_nested(data: Sequence[str]) -> bool:
    openings: List[int] = []
    closings: List[int] = []
    i: int = 0
    length: int = len(data)
    while i <= length - 1:
        if data[i] == '[':
            openings.append(i)
        else:
            closings.append(i)
        i += 1
    closings.reverse()
    x: int = 0
    y: int = 0
    z: int = len(closings)
    c: int = 0
    while x < len(openings):
        if y >= z:
            x += 1
            continue
        if openings[x] < closings[y]:
            c += 1
            y += 1
        x += 1
    return c >= 2