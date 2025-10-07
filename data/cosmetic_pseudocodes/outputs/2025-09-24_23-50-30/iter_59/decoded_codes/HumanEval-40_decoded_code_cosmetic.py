from typing import Sequence

def triples_sum_to_zero(param_a: Sequence[int]) -> bool:
    x = 0
    n = len(param_a)
    while x <= n - 1:
        y = x + 1
        while y <= n - 1:
            z = y + 1
            while z <= n - 1:
                if (param_a[x] + param_a[y] + param_a[z]) == 0:
                    return True
                z += 1
            y += 1
        x += 1
    return False