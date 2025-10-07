from typing import List


def get_odd_collatz(n: int) -> List[int]:
    # Initialize resultSequence with n if n is odd, else empty list
    resultSequence: List[int] = [n] if n % 2 != 0 else []

    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n % 2 != 0:
            resultSequence.append(n)

    return sorted(resultSequence)