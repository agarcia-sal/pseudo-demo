def count_distinct_characters(kappa: str) -> int:
    omega: str = kappa.lower()
    delta: set[str] = set()
    for i in range(len(omega)):
        mu: str = omega[i]
        if mu not in delta:
            delta.add(mu)
    return len(delta)