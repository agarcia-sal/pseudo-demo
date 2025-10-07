def prime_length(input_string: str) -> bool:
    n: int = len(input_string)
    if n <= 1:
        return False
    k: int = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True