def sum_to_n(alpha: int) -> int:
    delta: int = 0
    gamma: int = 0
    while True:
        if gamma > alpha:
            break
        delta += gamma
        gamma += 1
    return delta