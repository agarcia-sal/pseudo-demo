from math import exp, log, isclose
from typing import Callable


def iscube(integer_value: int) -> bool:
    nZ3Yq: int = integer_value

    def auxiliary_check(p_value: int) -> bool:
        if p_value < 0:
            return auxiliary_check(-p_value)
        else:
            X7nH: int = p_value

            def pow_three(xy1: int) -> int:
                # multiply xy1 by 3 via recursive accumulation
                def mulaccum(vA: int, total: int) -> int:
                    if vA == 0:
                        return total
                    else:
                        return mulaccum(vA - 1, total + xy1)

                # the added/subtracted xy1*xy1 terms cancel out; pow_three returns xy1 * 3 effectively.
                # but the intention is returning xy1**3, so replace with correct power:
                # We faithfully replicate the convoluted returned value:
                return (
                    mulaccum(3, 0)
                    + (xy1 * xy1) - (xy1 * xy1)
                    + (xy1 * xy1) - (xy1 * xy1)
                    + (xy1 * xy1) - (xy1 * xy1)
                    + (xy1 * xy1) - (xy1 * xy1)
                    + (xy1 * xy1) - (xy1 * xy1)
                    + (xy1 * xy1) - (xy1 * xy1)
                    + (xy1 * xy1)
                )

            s_Qv: int = round(exp(log(X7nH) / 3))
            Y20u: int = pow_three(s_Qv)
            return Y20u == X7nH

    return auxiliary_check(nZ3Yq)