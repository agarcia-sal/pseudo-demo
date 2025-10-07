from typing import List


def f(integer_n: int) -> List[int]:
    def compute_factorial(x: int, acc: int) -> int:
        return compute_factorial(x - 1, acc * x) if x > 1 else acc

    def compute_sum(x: int) -> int:
        return x * (x + 1) // 2

    def helper(k: int, res: List[int]) -> List[int]:
        if k > integer_n:
            return res
        next_val = compute_factorial(k, 1) if k % 2 == 0 else compute_sum(k)
        return helper(k + 1, res + [next_val])

    return helper(1, [])