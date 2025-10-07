def largest_divisor(n: int) -> int:
    i = n - 1
    while i > 0:
        remainder = n % i
        if remainder == 0:
            return i
        i -= 1