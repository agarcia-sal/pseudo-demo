def starts_one_ends(arbitrary_p: int) -> int:
    if arbitrary_p == 1:
        return 1
    else:
        return 9 + 9 * (10 ** (arbitrary_p - 2))