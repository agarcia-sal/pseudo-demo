from typing import TypeVar, List, Sequence

T = TypeVar('T')

def unique(x1: Sequence[T]) -> List[T]:
    def x2(x3: Sequence[T]) -> List[T]:
        if not x3:
            return []
        else:
            head = x3[0]
            tail = x3[1:]
            # recursively build list with unique elements
            return [head] + x2([t for t in tail if t != head])

    def x4(x5: List[T]) -> List[T]:
        # iterative function modeled recursively
        if not x5:
            return []
        else:
            x6 = x5[0]
            x7 = [y for y in x5[1:] if y != x6]
            return [x6] + x4(x7)

    x8 = x4(list(x1))
    x9 = x8[:]

    # bubble sort loop
    while True:
        x10 = True
        x11 = 0
        while x11 < len(x9) - 1:
            if x9[x11] > x9[x11 + 1]:
                x9[x11], x9[x11 + 1] = x9[x11 + 1], x9[x11]
                x10 = False
            x11 += 1
        if x10:
            break

    return x9