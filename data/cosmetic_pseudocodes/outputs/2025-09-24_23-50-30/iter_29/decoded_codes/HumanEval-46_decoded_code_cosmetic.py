from typing import List

def fib4(x: int) -> int:
    seq: List[int] = [0, 0, 2, 0]

    if x < 4:
        return seq[x]

    def loop(i: int) -> int:
        if i > x:
            return seq[-1]
        new_val = sum(seq[-4:])
        seq.append(new_val)
        seq.pop(0)
        return loop(i + 1)

    return loop(4)