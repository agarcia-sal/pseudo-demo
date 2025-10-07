from typing import Tuple


def simplify(dividend_frac: str, divisor_frac: str) -> bool:
    # Split fractions into numerator and denominator parts
    top_dividend, bottom_dividend = dividend_frac.split("/")
    top_divisor, bottom_divisor = divisor_frac.split("/")
    combined_top = int(top_dividend) * int(top_divisor)
    combined_bottom = int(bottom_dividend) * int(bottom_divisor)
    # Return True if combined_top is divisible by combined_bottom without remainder
    return combined_top % combined_bottom == 0