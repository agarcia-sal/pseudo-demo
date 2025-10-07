from typing import List


def get_odd_collatz(n: int) -> List[int]:
    if n <= 0:
        return []
    if n % 2 == 0:
        odd_collatz: List[int] = []
    else:
        odd_collatz = [n]

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        if n % 2 == 1:
            odd_collatz.append(n)

    return sorted(odd_collatz)