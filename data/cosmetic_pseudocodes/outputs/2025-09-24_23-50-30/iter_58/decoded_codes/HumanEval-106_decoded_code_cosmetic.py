from typing import List

def f(x: int) -> List[int]:
    y: List[int] = []

    def compute_factorial(z: int, acc: int) -> int:
        if z > 0:
            return compute_factorial(z - 1, acc * z)  # decrement z by 1
        else:
            return acc

    def sum_to(n: int) -> int:
        return sum(range(1, n + 1))  # sum from 1 to n inclusive

    def loop(m: int) -> None:
        if m > x:
            return
        else:
            if m % 2 != 0:  # m modulo 2 not equal to 0 means m is odd
                u = sum_to(m)
            else:
                u = compute_factorial(m, 1)
            y.append(u)
            loop(m + 1)

    loop(1)
    return y