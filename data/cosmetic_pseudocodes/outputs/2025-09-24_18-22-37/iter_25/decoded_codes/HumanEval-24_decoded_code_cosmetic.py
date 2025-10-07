def largest_divisor(num: int) -> int:
    counter = num - 1
    while counter > 0:
        remainder_val = num % counter
        if remainder_val == 0:
            return counter
        else:
            counter -= 1
    # In case no divisor found (num=1), return 0 as no divisor less than num
    return 0