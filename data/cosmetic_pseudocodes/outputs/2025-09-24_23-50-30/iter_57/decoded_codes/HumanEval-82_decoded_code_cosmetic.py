def prime_length(input_string: str) -> bool:
    n = len(input_string)
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True