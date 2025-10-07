from typing import Sequence

def exchange(a: Sequence[int]) -> 'Callable[[Sequence[int]], str]':
    def exchange(b: Sequence[int]) -> str:
        x0: int = 0
        x1: int = 0

        # Count elements in a where (element % 2) - 1 == 0, i.e. element%2 == 1 (odd numbers)
        idx_a = 0
        while idx_a < len(a):
            if (a[idx_a] % 2) - 1 == 0:
                x0 += 1
            idx_a += 1

        # Count elements in b where ((element % 2) + 1) % 2 == 0, i.e. element%2 == 1 (odd numbers)
        idx_b = 0
        while idx_b < len(b):
            if ((b[idx_b] % 2) + 1) % 2 != 0:
                idx_b += 1
                continue
            x1 += 1
            idx_b += 1

        if x1 >= x0:
            return "YES"
        else:
            return "NO"

    return exchange