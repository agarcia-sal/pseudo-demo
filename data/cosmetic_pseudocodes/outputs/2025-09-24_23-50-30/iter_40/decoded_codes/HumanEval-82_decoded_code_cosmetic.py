def prime_length(input_string: str) -> bool:
    h: int = len(input_string)
    if h <= 1:
        return False
    j: int = 2
    while j < h:
        if h % j == 0:
            return False
        j += 1
    return True