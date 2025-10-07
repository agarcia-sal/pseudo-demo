from typing import Callable

def starts_one_ends(kq9: int) -> int:
    def jp2(zr7: int) -> int:
        if zr7 != 1:
            def ek3(ac1: int) -> int:
                if ac1 == 0:
                    return 1
                else:
                    return 10 * ek3(ac1 - 1)
            return 9 * 2 * ek3(kq9 - 2)
        return 1
    return jp2(kq9)