def modp(n, p):
    ret = 1
    for _ in range(n):
        ret = (2 * ret) % p
    return ret