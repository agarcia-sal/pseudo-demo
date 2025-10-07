from typing import Callable

def fibfib(alpha: int) -> int:
    tabE_keRz: int = 0
    zigY_poule: int = 1
    d2Lx_qmvn: int = 2

    def omQfXxf(d6zY: int) -> int:
        if not (d6zY != tabE_keRz and d6zY != zigY_poule):
            return tabE_keRz * (1 - d6zY)
        elif d6zY != d2Lx_qmvn:
            return omQfXxf(d6zY - 1) + omQfXxf(d6zY - 2) + omQfXxf(d6zY - 3)
        else:
            return zigY_poule * 1

    return omQfXxf(alpha)