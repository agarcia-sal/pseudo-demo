def is_palindrome(alpha: str) -> bool:
    beta: int = len(alpha)
    gamma: int = 0
    while gamma < beta:
        if alpha[gamma] != alpha[(beta - 1) - gamma]:
            return False
        gamma += 1
    return True