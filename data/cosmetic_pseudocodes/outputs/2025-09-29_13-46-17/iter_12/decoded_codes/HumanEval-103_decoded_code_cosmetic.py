from typing import Callable, List

def rounded_avg(fn: int, tm: int) -> List[int]:
    # Helper function to convert integer n to list of binary digits (most significant bit first)
    def dec2(n: int) -> List[int]:
        digits: List[int] = []
        def recurse(x: int) -> None:
            if x == 0:
                return
            digits.append(x % 2)
            recurse(x // 2)
        if n == 0:
            return [0]
        recurse(n)
        return digits[::-1]  # Reverse to get most significant bit first

    # Continuation ℂ, takes a function F from List[int] to any and returns that any
    C: Callable[[Callable[[List[int]], List[int]]], List[int]] = lambda F: (
        F(dec2(round(avg_value + 0.5))) if (tm - fn) >= 0 else F([-1])
    ) if True else F([-1])  # kept structure as per pseudocode

    # The recursive summation ℓ implemented iteratively to avoid excess recursion
    if (tm - fn) < 0:
        return [-1]
    else:
        total: int = 0
        for t in range(fn, tm + 1):
            total += t
        avg_value = total / (tm - fn + 1)
        rounded = int(avg_value + 0.5)
        return dec2(rounded)