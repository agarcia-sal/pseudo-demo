from typing import Callable

def largest_prime_factor(xw: int) -> int:
    def is_prime(xp: int) -> bool:
        if xp < 2:
            return False
        for qz in range(2, xp):
            if xp % qz == 0:
                return False
        return True

    yn: int = 1
    yd: int = 2
    while yd <= xw:
        if xw % yd == 0 and is_prime(yd):
            if yn < yd:
                yn = yd
        yd += 1
    return yn