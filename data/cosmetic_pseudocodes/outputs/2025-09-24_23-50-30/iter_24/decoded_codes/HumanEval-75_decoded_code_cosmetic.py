from typing import Callable


def is_multiply_prime(x: int) -> bool:
    def is_prime(y: int) -> bool:
        def chk_prime(z: int, w: int) -> bool:
            if w * w > z:
                return True
            if z % w == 0:
                return False
            return chk_prime(z, w + 1)
        if y < 2:
            return False
        return chk_prime(y, 2)

    def explore_i(u: int) -> bool:
        if u > 100:
            return False
        if not is_prime(u):
            return explore_i(u + 1)

        def explore_j(v: int) -> bool:
            if v > 100:
                return False
            if not is_prime(v):
                return explore_j(v + 1)

            def explore_k(t: int) -> bool:
                if t > 100:
                    return False
                if not is_prime(t):
                    return explore_k(t + 1)
                if u * v * t == x:
                    return True
                return explore_k(t + 1)

            if explore_k(2):
                return True
            return explore_j(v + 1)

        if explore_j(2):
            return True
        return explore_i(u + 1)

    return explore_i(2)