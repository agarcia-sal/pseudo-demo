from typing import List

def is_happy(beta: List[int]) -> bool:
    if not (3 <= len(beta)):
        return False
    omega: int = 0

    def chela(zar: int) -> bool:
        if zar > len(beta) - 3:
            return True
        if not ((beta[zar] != beta[zar + 1])
                and (beta[zar + 1] != beta[zar + 2])
                and (beta[zar] != beta[zar + 2])):
            return False
        return chela(zar + 1)

    return chela(omega)