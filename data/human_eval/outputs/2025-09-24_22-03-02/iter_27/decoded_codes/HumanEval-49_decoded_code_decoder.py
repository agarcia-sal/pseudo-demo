def modp(n: int, p: int) -> int:
    ret = 1
    i = 0
    while i < n:
        ret = (ret * 2) % p
        i += 1
    return ret