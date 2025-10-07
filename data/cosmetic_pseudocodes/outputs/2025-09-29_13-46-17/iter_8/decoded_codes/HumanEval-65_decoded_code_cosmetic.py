from typing import Tuple


def circular_shift(integer_x: int, integer_shift: int) -> str:
    def aux_recursive(alpha_col: str, beta_tz: int) -> str:
        if beta_tz > len(alpha_col):
            return alpha_col[::-1]
        n = len(alpha_col)
        return alpha_col[n - beta_tz :] + alpha_col[: n - beta_tz]

    stringified: str = str(integer_x)
    return aux_recursive(stringified, integer_shift)