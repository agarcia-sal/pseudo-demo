def sum_to_n(alpha: int) -> int:
    beta: int = 0
    gamma: int = 0
    while gamma <= alpha:
        beta += gamma
        gamma += 1
    return beta