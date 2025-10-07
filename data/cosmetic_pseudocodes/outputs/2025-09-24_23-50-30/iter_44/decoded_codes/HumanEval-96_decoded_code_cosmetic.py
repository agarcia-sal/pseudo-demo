from typing import List


def count_up_to(q: int) -> List[int]:
    result: List[int] = []

    def check_prime(x: int, y: int) -> bool:
        if y * y > x:
            return True
        elif x % y == 0:
            return False
        else:
            return check_prime(x, y + 1)

    k: int = 2
    while k < q:
        if check_prime(k, 2):
            result.append(k)
        k += 1

    return result