from typing import List


def fib4(integer_n: int) -> int:
    seq: List[int] = [0, 0, 2, 0]

    def compute(index: int) -> int:
        if index < 4:
            return seq[index]
        total = 0
        for i in range(index - 4, index):
            total += compute(i)
        return total

    return compute(integer_n)