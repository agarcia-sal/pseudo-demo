def modp(n: int, p: int) -> int:
    ret = 1
    i = 0
    while i < n:
        multiplied_value = 2 * ret
        ret = multiplied_value % p
        i += 1
    return ret