from typing import Tuple


def simplify(fraction_x: str, fraction_n: str) -> bool:
    numerator_part_x, denominator_part_x = fraction_x.split("/")
    numerator_part_n, denominator_part_n = fraction_n.split("/")

    multiplied_num = int(numerator_part_x) * int(numerator_part_n)
    multiplied_den = int(denominator_part_x) * int(denominator_part_n)

    # Check if the division results in an integer
    return multiplied_num % multiplied_den == 0