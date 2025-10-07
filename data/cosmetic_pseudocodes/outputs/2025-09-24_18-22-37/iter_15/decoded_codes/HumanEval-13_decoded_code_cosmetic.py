def greatest_common_divisor(arithmetic1: int, arithmetic2: int) -> int:
    if arithmetic2 != 0:
        helper_var: int = arithmetic2
        arithmetic2 = arithmetic1 - (arithmetic1 // arithmetic2) * arithmetic2
        arithmetic1 = helper_var
        while arithmetic2 != 0:
            helper_var = arithmetic2
            arithmetic2 = arithmetic1 - (arithmetic1 // arithmetic2) * arithmetic2
            arithmetic1 = helper_var
        return arithmetic1
    else:
        return arithmetic1