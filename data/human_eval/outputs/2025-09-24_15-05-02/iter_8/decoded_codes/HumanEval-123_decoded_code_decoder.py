from typing import List

def get_odd_collatz(n: int) -> List[int]:
    odd_collatz: List[int] = [] if n % 2 == 0 else [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        if n % 2 == 1:
            odd_collatz.append(n)
    return sorted(odd_collatz)