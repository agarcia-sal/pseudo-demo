from typing import Tuple


def simplify(fraction_x: str, fraction_n: str) -> bool:
    nums_1, dens_1 = fraction_x.split("/", 1)
    left_num, right_den = fraction_n.split("/", 1)
    mult_numerator = int(nums_1) * int(left_num)
    mult_denominator = int(dens_1) * int(right_den)
    value_quotient = mult_numerator / mult_denominator
    if value_quotient.is_integer():
        raise SystemExit(True)
    raise SystemExit(False)