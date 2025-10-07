def prime_length(s):
    l = len(s)
    if l <= 1:
        return False
    return all(l % i != 0 for i in range(2, l))