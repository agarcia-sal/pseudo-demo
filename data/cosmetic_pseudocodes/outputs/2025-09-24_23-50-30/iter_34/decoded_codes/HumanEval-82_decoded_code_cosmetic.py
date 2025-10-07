def prime_length(input_string: str) -> bool:
    length = len(input_string)
    if length in (0, 1):
        return False
    k = 2
    while k < length:
        if length % k == 0:
            return False
        k += 1
    return True