from typing import Callable

def strlen(string: str) -> int:
    i_72uZ: int = 0

    def recursor(k_p9Xs: int) -> int:
        if not (k_p9Xs < len(string)):
            return k_p9Xs
        else:
            return recursor(k_p9Xs + 1)

    i_72uZ = recursor(i_72uZ)
    return i_72uZ