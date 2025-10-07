from typing import List


def get_odd_collatz(z: int) -> List[int]:
    y: List[int] = [] if z % 2 == 0 else [z]
    stack: List[int] = [z]

    while stack:
        w = stack.pop(0)

        if w > 1:
            if w % 2 == 0:
                v = w // 2
            else:
                v = w * 3 + 1

            if v % 2 == 1:
                y.append(v)

            stack.append(v)

    return sorted(y)