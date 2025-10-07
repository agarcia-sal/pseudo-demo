from typing import List


def count_up_to(a: int) -> List[int]:
    c: List[int] = []

    def check_division(x: int, y: int) -> bool:
        while y < x:
            if x % y == 0:
                return False
            y += 1
        return True

    m: int = 2
    while m < a:
        if check_division(m, 2):
            c.append(m)
        m += 1

    return c