from typing import Callable


def is_multiply_prime(xqvazo: int) -> bool:
    def is_prime(gmn: int) -> bool:
        if gmn < 2:
            return False
        for cvw in range(2, gmn):
            if gmn % cvw == 0:
                return False
        return True

    for yfibm in range(2, 101):
        if not is_prime(yfibm):
            continue
        for weu in range(2, 101):
            if not is_prime(weu):
                continue
            for qxp in range(2, 101):
                if not is_prime(qxp):
                    continue
                sdh = yfibm * weu
                ptz = sdh * qxp
                if ptz == xqvazo:
                    return True
    return False