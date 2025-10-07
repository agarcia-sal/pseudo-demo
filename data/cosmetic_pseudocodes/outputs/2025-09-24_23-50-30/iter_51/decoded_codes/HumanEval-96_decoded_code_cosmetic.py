from typing import List


def count_up_to(u: int) -> List[int]:
    v: List[int] = []

    def w(x: int, y: int) -> bool:
        if y >= x:
            return True
        if x % y == 0:
            return False
        return w(x, y + 1)

    def z(a: int, b: int) -> None:
        if a >= b:
            return
        if w(a, 2):
            v.append(a)
        z(a + 1, b)

    z(2, u)
    return v