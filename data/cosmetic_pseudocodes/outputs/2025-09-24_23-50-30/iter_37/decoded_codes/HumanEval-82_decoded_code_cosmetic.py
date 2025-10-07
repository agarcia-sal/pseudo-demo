def prime_length(input_string: str) -> bool:
    count: int = len(input_string)
    if count <= 1:
        return False
    divisor: int = 2
    while divisor < count:
        if count % divisor == 0:
            return False
        divisor += 1
    return True