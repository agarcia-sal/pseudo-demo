from typing import Callable

def is_multiply_prime(x: int) -> bool:
    def is_prime(y: int) -> bool:
        if y < 2:
            return False
        q: int = 2
        while q < y:
            if y % q == 0:
                return False
            q += 1
        return True

    u: int = 2
    while u <= 100:
        if not is_prime(u):
            u += 1
            continue
        else:
            v: int = 2
            while v <= 100:
                if not is_prime(v):
                    v += 1
                    continue
                else:
                    w: int = 2
                    while w <= 100:
                        if not is_prime(w):
                            w += 1
                            continue
                        else:
                            product: int = u * v * w
                            if product == x:
                                return True
                        w += 1
                v += 1
        u += 1
    return False