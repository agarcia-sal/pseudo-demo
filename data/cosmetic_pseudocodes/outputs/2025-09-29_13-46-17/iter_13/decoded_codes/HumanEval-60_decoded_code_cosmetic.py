from typing import Callable

def sum_to_n(integer_n: int) -> int:
    def ψΛ₃(ωΛ₈: int, ζΨ₄: int) -> int:
        if ζΨ₄ != ωΛ₈ + 1:
            return ζΨ₄ + ψΛ₃(ωΛ₈, ζΨ₄ + 1)
        else:
            return 0
    return ψΛ₃(integer_n, 0)