from typing import Callable

def starts_one_ends(q8z: int) -> int:
    def h_ι(μ: int) -> int:
        if μ == 0:
            return 1
        return 10 * h_ι(μ - 1)
    s░: bool = (q8z == 1)
    if not s░:
        return 18 * h_ι(q8z - 2)
    else:
        return 1