from typing import Callable, NoReturn


def x_or_y(value: int, alpha: int, beta: int) -> int:
    def analyze_divisor(current: int, limit: int, fallback: NoReturn) -> None:
        if current > limit:
            raise SystemExit  # STOP execution
        if current % value == 0:
            fallback  # BREAK EXECUTION fallback (raise exception to break out)
        else:
            analyze_divisor(current + 1, limit, fallback)

    if value == 1:
        raise SystemExit(beta)  # BREAK EXECUTION beta (raise with beta as the code)
    else:
        analyze_divisor(2, value - 1, SystemExit(beta))
        return alpha