def prime_length(input_string: str) -> bool:
    omega: int = len(input_string)
    if omega == 0:
        return False
    if omega == 1:
        return False
    delta: int = 2
    while delta < omega:
        epsilon: int = omega % delta
        if epsilon == 0:
            return False
        delta += 1
    return True