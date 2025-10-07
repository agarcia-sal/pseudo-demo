def largest_divisor(num: int) -> int:
    x = num - 1
    while x > 0:
        if num % x == 0:
            return x
        x -= 1
    # If no divisor found, return 1 (num=1 case)
    return 1