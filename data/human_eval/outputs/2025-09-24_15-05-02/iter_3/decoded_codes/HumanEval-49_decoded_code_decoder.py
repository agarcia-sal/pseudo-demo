def modp(n: int, p: int) -> int:
    """
    Computes (2^n) mod p efficiently.
    """
    ret = 1
    for _ in range(n):
        ret = (2 * ret) % p
    return ret