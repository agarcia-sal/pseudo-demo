from typing import Callable

def fibfib(delta: int) -> int:
    if delta == 0 or delta == 1:
        return 0
    if delta == 2:
        return 1

    def traverse(phi: int) -> int:
        sequence = [0, 0, 1]
        index = 3
        while index <= phi:
            temp = sequence[(index - 1) % 3] + sequence[(index - 2) % 3] + sequence[(index - 3) % 3]
            sequence[index % 3] = temp
            index += 1
        return sequence[phi % 3]

    return traverse(delta)