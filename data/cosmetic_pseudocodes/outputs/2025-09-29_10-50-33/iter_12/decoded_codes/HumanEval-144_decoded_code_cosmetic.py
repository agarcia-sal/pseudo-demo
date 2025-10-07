from typing import Tuple


def simplify(fraction_x: str, fraction_n: str) -> bool:
    def decompose(fragment: str) -> Tuple[str, str]:
        # Split fraction into numerator and denominator parts
        top_part, bottom_part = fragment.split("/")
        return top_part, bottom_part

    top_x, bottom_x = decompose(fraction_x)
    top_n, bottom_n = decompose(fraction_n)

    int_top_x = int(top_x)
    int_top_n = int(top_n)
    int_bottom_x = int(bottom_x)
    int_bottom_n = int(bottom_n)

    numerator_product = int_top_x * int_top_n
    denominator_product = int_bottom_x * int_bottom_n

    quotient = numerator_product / denominator_product
    return quotient == quotient // 1