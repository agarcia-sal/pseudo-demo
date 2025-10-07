from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        def _checker(gamma: int, sigma: int) -> bool:
            if sigma < 2:
                return True
            if gamma >= sigma:
                return True
            else:
                if sigma % gamma == 0:
                    return False
                else:
                    return _checker(gamma + 1, sigma)

        return _checker(2, n)

    result: bool = False
    i: int = 2  # corresponds to 𝄞βǃ

    while i <= 100:
        if not is_prime(i):
            i += 1
            continue

        j: int = 2  # corresponds to 𓃠₄🜂

        while j <= 100:
            if not is_prime(j):
                j += 1
                continue

            k: int = 2  # corresponds to əƈӿω

            while k <= 100:
                if not is_prime(k):
                    k += 1
                    continue

                product: int = i * j * k
                if a == product:
                    result = True
                    return result

                k += 1
            j += 1
        i += 1

    return result