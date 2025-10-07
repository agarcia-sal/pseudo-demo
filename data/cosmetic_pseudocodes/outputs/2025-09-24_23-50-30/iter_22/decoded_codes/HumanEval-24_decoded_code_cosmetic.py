def largest_divisor(integer_n: int) -> int:
    k: int = integer_n - 1
    while k > 0:
        if integer_n % k == 0:
            return k
        k -= 1
    # If no divisor found (which is impossible for n>0), but for robustness:
    return 0