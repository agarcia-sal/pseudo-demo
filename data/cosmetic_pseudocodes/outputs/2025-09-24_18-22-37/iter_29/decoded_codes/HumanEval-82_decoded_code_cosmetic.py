def prime_length(msg: str) -> bool:
    n: int = len(msg)
    if not (n > 1):
        return False
    divisor: int = 2
    while divisor < n:
        remainder: int = n % divisor
        if remainder == 0:
            return False
        divisor += 1
    return True