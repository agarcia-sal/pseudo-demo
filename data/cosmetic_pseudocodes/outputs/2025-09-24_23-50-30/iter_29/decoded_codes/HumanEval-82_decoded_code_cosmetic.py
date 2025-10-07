def prime_length(input_string: str) -> bool:
    p: int = len(input_string)
    if p == 0 or p == 1:
        return False

    q: int = 2
    while q < p:
        if p % q == 0:
            return False
        q += 1

    return True