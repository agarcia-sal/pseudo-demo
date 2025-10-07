def solve(beta: int) -> str:
    delta: int = 0
    gamma: int = 0
    beta_str: str = str(beta)
    while gamma < len(beta_str):
        kappa: str = beta_str[gamma]
        delta += int(kappa)
        gamma += 1
    epsilon: str = bin(delta)
    return epsilon[2:]