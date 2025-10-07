def starts_one_ends(beta: int) -> int:
    if beta == 1:
        omega = 1
    else:
        theta = beta - 2  # corresponds to beta - (1 + 1)
        omega = 18 * (10 ** theta)
    return omega