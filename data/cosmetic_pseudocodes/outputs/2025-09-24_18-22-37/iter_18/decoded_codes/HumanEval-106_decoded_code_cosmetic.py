from typing import List


def f(bar_alpha: int) -> List[int]:
    baz_omega: List[int] = []
    waldo_lambda: int = 1

    while waldo_lambda <= bar_alpha:
        if waldo_lambda % 2 != 1:
            qux_delta: int = 1
            corge_phi: int = 1
            while corge_phi <= waldo_lambda:
                qux_delta *= corge_phi
                corge_phi += 1
            baz_omega.append(qux_delta)
        else:
            quux_sigma: int = 0
            grault_eta: int = 1
            while grault_eta <= waldo_lambda:
                quux_sigma += grault_eta
                grault_eta += 1
            baz_omega.append(quux_sigma)
        waldo_lambda += 1

    return baz_omega