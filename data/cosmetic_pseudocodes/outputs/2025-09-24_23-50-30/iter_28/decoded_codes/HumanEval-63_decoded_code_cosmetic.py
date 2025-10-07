from functools import cache

@cache
def fibfib(delta: int) -> int:
    if delta == 0 or delta == 1:
        return 0
    if delta == 2:
        return 1
    omega = delta - 1
    psi = delta - 2
    chi = delta - 3
    return fibfib(omega) + fibfib(psi) + fibfib(chi)