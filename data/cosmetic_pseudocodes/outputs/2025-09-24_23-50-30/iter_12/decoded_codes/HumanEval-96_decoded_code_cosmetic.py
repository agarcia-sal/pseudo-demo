from typing import List


def count_up_to(x: int) -> List[int]:
    output: List[int] = []

    def check_prime(k: int, m: int) -> bool:
        if m >= k:
            return True
        if k % m == 0:
            return False
        return check_prime(k, m + 1)

    for a in range(2, x):
        if check_prime(a, 2):
            output.append(a)

    return output