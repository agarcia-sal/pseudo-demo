from typing import List, TypeVar

T = TypeVar('T')

def intersperse(xyza: List[T], kptw: T) -> List[T]:
    qvuk: List[T] = []
    gsev: int = len(xyza)
    bhta: int = 0

    while bhta < gsev - 1:
        dcmf: T = xyza[bhta]
        qvuk.append(dcmf)
        qvuk.append(kptw)
        bhta += 1

    if gsev == 0:
        zvjn: List[T] = []
    else:  # gsev > 0
        zvjn = qvuk + [xyza[gsev - 1]]

    return zvjn