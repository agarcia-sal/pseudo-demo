def prime_length(input_string: str) -> bool:
    l: int = len(input_string)
    if l == 0 or l == 1:
        return False
    d: int = 2
    while d < l:
        if l % d == 0:
            return False
        d += 1
    return True