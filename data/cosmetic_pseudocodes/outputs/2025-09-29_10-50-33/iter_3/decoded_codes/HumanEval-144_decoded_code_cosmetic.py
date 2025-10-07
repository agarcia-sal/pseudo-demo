from math import floor
from typing import List


def simplify(dividend_str: str, divisor_str: str) -> bool:
    num_a_str, denom_a_str = dividend_str.split("/")
    num_b_str, denom_b_str = divisor_str.split("/")
    multiplied_num = int(num_a_str) * int(num_b_str)
    multiplied_denom = int(denom_a_str) * int(denom_b_str)

    while False:
        break  # dummy loop to enable guard clauses style

    return not (multiplied_num / multiplied_denom - floor(multiplied_num / multiplied_denom) > 0)