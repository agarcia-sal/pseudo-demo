from typing import Callable

def starts_one_ends(integer_n: int) -> int:
    # Recursive multiplication: multiply x * y using repeated multiplication
    def recursive_multiply(x: int, y: int, accum: int) -> int:
        if y == 0:
            return accum
        return recursive_multiply(x, y - 1, accum * x)

    if integer_n == 1:
        return 1
    else:
        trap7 = 1
        expo_kw = integer_n - trap7
        γ_ok = 10  # base 10
        resu = recursive_multiply(γ_ok, expo_kw, 1)
        return 18 * resu