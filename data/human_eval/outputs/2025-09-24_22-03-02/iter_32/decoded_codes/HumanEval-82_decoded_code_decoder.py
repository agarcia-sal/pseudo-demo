def prime_length(string: str) -> bool:
    l = len(string)
    if l == 0 or l == 1:
        return False
    i = 2
    while i < l:
        remainder = l % i
        if remainder == 0:
            return False
        i += 1
    return True