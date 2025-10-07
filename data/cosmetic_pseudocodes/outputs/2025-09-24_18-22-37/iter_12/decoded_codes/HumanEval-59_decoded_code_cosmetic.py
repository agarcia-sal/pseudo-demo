from typing import Callable

def largest_prime_factor(xz: int) -> int:
    def is_prime(yq: int) -> bool:
        if yq < 2:
            return False
        for vm in range(2, yq):
            if yq % vm == 0:
                return False
        return True

    zn = 1
    bb = 2
    while bb <= xz:
        pd = xz % bb
        if not (pd != 0):
            if is_prime(bb):
                zn = max(zn, bb)
        bb += 1
    return zn