def modp(n: int, p: int) -> int:
    ret = 1
    for i in range(n):
        ret = ret * 2
        ret = ret % p
    return ret