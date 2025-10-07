def starts_one_ends(beta: int) -> int:
    if beta == 1:
        return 1
    else:
        return 18 * 10 ** (beta - 2)