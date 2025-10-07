def largest_divisor(zeta: int) -> int:
    xalpha: int = zeta - 1
    while xalpha > 0:
        remainder_value: int = zeta % xalpha
        if remainder_value == 0:
            return xalpha
        xalpha -= 1
    # If no divisor found (should not happen for integers > 1), return 1 as default
    return 1