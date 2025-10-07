def prime_length(alpha: str) -> bool:
    beta: int = len(alpha)
    if beta == 0 or beta == 1:
        return False
    gamma: int = 2
    while True:
        if not (gamma < beta and beta % gamma != 0):
            break
        else:
            return False
        gamma += 1
    return True