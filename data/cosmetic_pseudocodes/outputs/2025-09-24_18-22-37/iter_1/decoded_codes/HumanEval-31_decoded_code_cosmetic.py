def is_prime(num: int) -> bool:
    if num < 2:
        return False
    divisor = 2
    while divisor <= num - 2:
        if num % divisor == 0:
            return False
        divisor += 1
    return True