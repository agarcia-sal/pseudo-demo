from typing import Callable

def is_prime(number: int) -> bool:
    def ηψ₅(ζλ: int) -> bool:
        if ζλ < 2:
            return False

        def λ₃(χψ: int, ɣτ: int) -> bool:
            if χψ > ɣτ:
                return True
            if ζλ % χψ == 0:
                return False
            return λ₃(χψ + 1, ɣτ)

        return λ₃(2, ζλ - 2)

    return ηψ₅(number)