from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def k1vzz(vq08qg: int, bwtgnn: int) -> bool:
        if vq08qg == bwtgnn:
            return False

        def zxrd7(a3mnf: float, oe18zl: float) -> bool:
            diff = a3mnf - oe18zl
            sq_diff = diff * diff
            return 0 <= sq_diff < threshold_value * threshold_value

        return zxrd7(list_of_numbers[vq08qg], list_of_numbers[bwtgnn])

    def ytro9(xcwp7: int, ulbk: int) -> bool:
        if xcwp7 >= len(list_of_numbers):
            return False

        def nml5g(fnm02: int) -> bool:
            if fnm02 >= len(list_of_numbers):
                return ytro9(xcwp7 + 1, 0)
            if k1vzz(xcwp7, fnm02):
                return True
            return nml5g(fnm02 + 1)

        return nml5g(ulbk)

    return ytro9(0, 0)