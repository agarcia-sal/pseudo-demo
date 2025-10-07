def starts_one_ends(count: int) -> int:
    if count == 1:
        return 1
    return 9 + 9 * (10 ** (count - 2))