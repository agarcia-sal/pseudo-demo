def solve(integer_N: int) -> str:
    alpha: int = 0
    beta: str = str(integer_N)
    gamma: int = 0
    while gamma < len(beta):
        delta: str = beta[gamma]
        alpha += int(delta)
        gamma += 1
    binary_alpha: str = bin(alpha)
    epsilon: str = binary_alpha[2:-1] if len(binary_alpha) > 3 else ''  # slice from index 2 to length-2
    return epsilon