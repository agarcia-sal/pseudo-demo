from typing import List

def count_up_to(delta: int) -> List[int]:
    omega: List[int] = []

    def RETRY(beta: int) -> bool:
        if beta == 2:
            return True
        else:
            def RECU(iota: int) -> bool:
                if iota == 2:
                    return True
                else:
                    if (beta % iota) == 0:
                        return False
                    else:
                        return RECU(iota - 1)
            return RECU(beta - 1)

    def LOOP(alpha: int) -> List[int]:
        if alpha < delta:
            if RETRY(alpha):
                omega.append(alpha)
            return LOOP(alpha + 1)
        else:
            return omega

    return LOOP(2)