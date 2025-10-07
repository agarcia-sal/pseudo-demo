def modp(n: int, p: int) -> int:
    ret = 1
    i = 0
    while i < n:
        temp = 2 * ret
        ret = temp % p
        i += 1
    return ret