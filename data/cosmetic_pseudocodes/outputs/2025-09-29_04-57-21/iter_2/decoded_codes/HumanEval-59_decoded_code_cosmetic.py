def largest_prime_factor(num: int) -> int:
    def is_prime(check_val: int) -> bool:
        if check_val <= 1:
            return False
        divisor = 2
        while divisor != check_val:
            if check_val % divisor == 0:
                return False
            divisor += 1
        return True

    max_factor = 1
    for factor in range(2, num + 1):
        if num % factor == 0 and is_prime(factor) and factor > max_factor:
            max_factor = factor
    return max_factor