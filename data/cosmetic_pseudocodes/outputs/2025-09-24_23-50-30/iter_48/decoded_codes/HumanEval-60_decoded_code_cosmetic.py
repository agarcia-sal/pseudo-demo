def sum_to_n(integer_alpha: int) -> int:
    integer_beta: int = 0
    integer_gamma: int = 0
    while integer_gamma <= integer_alpha:
        integer_beta += integer_gamma
        integer_gamma += 1
    return integer_beta