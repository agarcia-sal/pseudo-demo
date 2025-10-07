def sum_to_n(delta: int) -> int:
    omega: int = 0
    psi: int = 0
    while psi <= delta:
        omega += psi
        psi += 1
    return omega