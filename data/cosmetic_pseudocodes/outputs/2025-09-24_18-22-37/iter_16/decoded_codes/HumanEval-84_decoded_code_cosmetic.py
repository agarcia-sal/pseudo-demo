def solve(beta: int) -> str:
    omega: int = 0
    gamma: str = str(beta)
    chi: int = 0
    while chi < len(gamma):
        zeta: str = gamma[chi]
        delta: int = int(zeta)
        omega += delta
        chi += 1
    epsilon: str = bin(omega)
    theta: str = epsilon[2:]
    return theta