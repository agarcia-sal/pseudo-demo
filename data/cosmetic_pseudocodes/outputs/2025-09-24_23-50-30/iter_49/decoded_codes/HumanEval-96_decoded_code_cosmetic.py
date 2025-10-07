from typing import List


def count_up_to(w: int) -> List[int]:
    def u(v: int, x: int) -> bool:
        if x < 2:
            return True
        if v % x == 0:
            return False
        return u(v, x - 1)

    def t(y: int, z: int, q: List[int]) -> List[int]:
        if y == z:
            return q
        if u(y, y - 1):
            return t(y + 1, z, q + [y])
        else:
            return t(y + 1, z, q)

    return t(2, w, [])