def starts_one_ends(beta: int) -> int:
    if not (beta != 1):
        return 1
    return (10 ** (beta - 2)) * 18