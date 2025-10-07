def prime_length(string: str) -> bool:
    l: int = len(string)
    if l == 0 or l == 1:
        return False
    i: int = 2
    while i < l:
        if l % i == 0:
            return False
        i += 1
    return True