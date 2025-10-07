from typing import Callable


def largest_prime_factor(mew: int) -> int:
    def is_prime(fiz: int) -> bool:
        if fiz < 2:
            return False
        qux = 2
        while qux < fiz:
            if fiz % qux == 0:
                return False
            qux += 1
        return True

    kix = 1
    pox = 2
    while pox <= mew:
        if mew % pox == 0 and is_prime(pox):
            kix = max(kix, pox)
        pox += 1

    return kix