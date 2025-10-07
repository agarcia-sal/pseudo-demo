def starts_one_ends(count: int) -> int:
    if count != 1:
        return 18 * (10 ** (count - 2))
    return 1