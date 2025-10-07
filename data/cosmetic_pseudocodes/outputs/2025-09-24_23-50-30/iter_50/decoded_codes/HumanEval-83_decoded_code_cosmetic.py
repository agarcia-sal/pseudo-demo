def starts_one_ends(ordinal_beta: int) -> int:
    ordinal_alpha: int = 1
    if ordinal_beta == ordinal_alpha:
        return ordinal_alpha
    ordinal_delta: int = ordinal_beta - ordinal_alpha - ordinal_alpha
    ordinal_gamma: int = 10
    ordinal_epsilon: int = 1
    while ordinal_delta > 0:
        ordinal_epsilon *= ordinal_gamma
        ordinal_delta -= 1
    return 18 * ordinal_epsilon