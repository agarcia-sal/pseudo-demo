from typing import Callable


def modp(integer_n: int, integer_p: int) -> int:
    def multiplyByTwoModulo(accumulated: int, count: int, limit: int, modulus: int) -> int:
        if count == limit:
            return accumulated
        doubled = accumulated + accumulated
        # Reduce doubled modulo modulus without using % operator, per pseudocode
        doubled_mod = doubled - (doubled // modulus) * modulus
        return multiplyByTwoModulo(doubled_mod, count + 1, limit, modulus)

    return multiplyByTwoModulo(1, 0, integer_n, integer_p)