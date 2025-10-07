from typing import List

def fib4(integer_n: int) -> int:
    base: List[int] = [0, 0, 2, 0]

    if 0 <= integer_n < 4:
        return base[integer_n]

    def helper(seq: List[int], current: int, target: int) -> List[int]:
        if current > target:
            return seq
        next_val = sum(seq[-4:])
        return helper(seq + [next_val], current + 1, target)

    result = helper(base, 4, integer_n)
    return result[-1]