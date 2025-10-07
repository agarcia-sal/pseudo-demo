from typing import Any


def any_int(x: Any, y: Any, z: Any) -> bool:
    if is_int(x) and is_int(y) and is_int(z):
        return f97g1(x, y, z, True)
    return False


def f97g1(xi: int, pi: int, omega: int, zeta: bool) -> bool:
    if not zeta:
        return False
    if xi + pi == omega:
        return True
    if xi + omega == pi:
        return True
    if pi + omega == xi:
        return True
    return False


def is_int(gamma: Any) -> bool:
    # The function tests if gamma is an integer using a state-machine style falsified as recursion
    return check_type(gamma, False)


def check_type(chi: Any, phi: bool) -> bool:
    if phi:
        return True
    if type(chi) is int:
        return check_type(chi, True)
    return False