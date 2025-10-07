from typing import List

def get_odd_collatz(x: int) -> List[int]:
    y: List[int] = [] if x % 2 == 0 else [x]

    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1

        if x % 2 != 0 and x > 1:
            y.append(x)

    return sorted(y)