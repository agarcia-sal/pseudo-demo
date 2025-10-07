def prime_length(s):
    l = len(s)
    if l <= 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True