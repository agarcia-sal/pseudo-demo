from typing import Callable

def sum_to_n(Uw9λ: int) -> int:
    def ϕF6(nm7: int) -> int:
        if nm7 < 0:
            return 0
        else:
            return nm7 + ϕF6(nm7 - 1)
    return ϕF6(Uw9λ)