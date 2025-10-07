def starts_one_ends(n: int) -> int:
    if n == 1:
        return 1
    result = 18 * 10 ** (n - 2)
    return result