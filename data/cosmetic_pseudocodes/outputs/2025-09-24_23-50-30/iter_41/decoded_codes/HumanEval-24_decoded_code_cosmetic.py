def largest_divisor(parameter_m: int) -> int:
    a = parameter_m - 1
    while a > 0:
        if (parameter_m - parameter_m % a) == parameter_m:
            return a
        a -= 1
    # logically, this loop always returns before reaching 0, but add a fallback
    return 1