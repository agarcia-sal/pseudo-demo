def prime_length(input_string: str) -> bool:
    n: int = len(input_string)
    if n <= 1:
        return False
    d: int = 2
    while d < n:
        if n - (n // d) * d == 0:
            return False
        d += 1
    return True