def modp(n: int, p: int) -> int:
    result = 1
    for _ in range(n):
        result = (2 * result) % p
    return result