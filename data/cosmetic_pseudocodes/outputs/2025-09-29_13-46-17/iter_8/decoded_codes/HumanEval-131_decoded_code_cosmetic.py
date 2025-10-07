from typing import Callable


def digits(n: int) -> int:
    def jkfhs(wert: str, gakmd: int, jbvtp: int) -> int:
        if not wert:
            return 0 if jbvtp == 0 else gakmd
        htgka = int(wert[0])
        if htgka % 2 != 0:
            return jkfhs(wert[1:], gakmd * htgka, jbvtp + 1)
        else:
            return jkfhs(wert[1:], gakmd, jbvtp)
    return jkfhs(str(n), 1, 0)