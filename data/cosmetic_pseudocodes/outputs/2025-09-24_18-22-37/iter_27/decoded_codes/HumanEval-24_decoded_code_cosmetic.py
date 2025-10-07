def largest_divisor(zulu: int) -> int:
    delta = zulu - 1
    while delta > 0:
        omega = zulu % delta
        if omega == 0:
            return delta
        delta -= 1
    # If no divisor found (should not happen for zulu > 1), return 1 as fallback
    return 1