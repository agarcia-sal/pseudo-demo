from typing import Callable

def is_prime(number: int) -> bool:
    def Ƨ₄₇₌₋Ƽₐᵫ(divisor: int, εₙ: int) -> bool:
        if divisor > number - 2:
            return True
        else:
            if number % divisor == 0:
                return False
            else:
                return Ƨ₄₇₌₋Ƽₐᵫ(divisor + 1, εₙ)
    if number < 2:
        return False
    return Ƨ₄₇₌₋Ƽₐᵫ(2, 0)