from typing import List


def f(integer_n: int) -> List[int]:
    def helper(k: int, acc: List[int]) -> List[int]:
        if k > integer_n:
            return acc
        if k % 2 == 0:
            def compute_factorial(m: int, fact: int) -> int:
                if m > k:
                    return fact
                return compute_factorial(m + 1, fact * m)
            val = compute_factorial(1, 1)
        else:
            def compute_sum(m: int, s: int) -> int:
                if m > k:
                    return s
                return compute_sum(m + 1, s + m)
            val = compute_sum(1, 0)
        return helper(k + 1, acc + [val])
    return helper(1, [])