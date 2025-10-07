def prime_length(string) -> bool:
    l = len(string)
    if l == 0 or l == 1:
        return False
    i = 2
    while i < l:
        if l % i == 0:
            return False
        i += 1
    return True