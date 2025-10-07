def largest_divisor(n: int) -> int:
    for i in range(n - 1, 0, -1):
        remainder = n % i
        if remainder == 0:
            return i