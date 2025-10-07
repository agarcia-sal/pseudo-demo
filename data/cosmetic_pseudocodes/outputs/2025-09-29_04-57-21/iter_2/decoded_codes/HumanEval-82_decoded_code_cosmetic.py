def prime_length(input_string: str) -> bool:
    size: int = len(input_string)
    if size <= 1:
        return False
    divisor_candidate: int = 2
    while divisor_candidate <= size - 1:
        if size - (size // divisor_candidate) * divisor_candidate == 0:
            return False
        divisor_candidate += 1
    return True