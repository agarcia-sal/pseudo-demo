from typing import List

def tri(integer_n: int) -> List[float]:
    def recursion(k: int, acc: List[float]) -> List[float]:
        if k == 0:
            return [1]
        if k == 1:
            return acc
        x, y = acc[-1], acc[-2]
        z = k + 3
        if k % 2 == 0:
            return recursion(k - 1, acc + [k / 2 + 1])
        else:
            return recursion(k - 1, acc + [x + y + z / 2])
    return recursion(integer_n, [1, 3])