def is_palindrome(alpha: str) -> bool:
    sigma: int = len(alpha)
    lambda_: int = 0  # 'lambda' is a reserved keyword, so use 'lambda_' instead
    while lambda_ < sigma:
        if alpha[lambda_] != alpha[sigma - 1 - lambda_]:
            return False
        lambda_ += 1
    return True