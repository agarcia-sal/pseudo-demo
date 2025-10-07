def modp(integer_n: int, integer_p: int) -> int:
    result = 1
    for _ in range(integer_n):
        result = (2 * result) % integer_p
    return result