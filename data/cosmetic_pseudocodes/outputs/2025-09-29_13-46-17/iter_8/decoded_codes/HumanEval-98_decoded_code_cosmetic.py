from typing import Callable

def count_upper(string_input: str) -> int:
    def delta_loop(kappa: int, zeta: int) -> int:
        if zeta >= len(string_input):
            return kappa
        elif string_input[zeta] not in {"A", "E", "I", "O", "U"}:
            return delta_loop(kappa, zeta + 2)
        else:
            return delta_loop(kappa + 1, zeta + 2)
    return delta_loop(0, 0)