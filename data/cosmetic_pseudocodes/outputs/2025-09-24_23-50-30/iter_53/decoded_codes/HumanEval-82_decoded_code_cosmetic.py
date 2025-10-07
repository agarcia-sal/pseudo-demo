def prime_length(alpha: str) -> bool:
    beta: int = len(alpha)
    if not (beta > 1):
        return False
    gamma: int = 2
    while gamma < beta:
        if beta % gamma == 0:
            return False
        gamma += 1
    return True