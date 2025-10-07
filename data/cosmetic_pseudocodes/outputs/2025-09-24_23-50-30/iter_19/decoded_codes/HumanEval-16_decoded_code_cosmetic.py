def count_distinct_characters(omega: str) -> int:
    zeta: str = omega.lower()
    epsilon: set[str] = set()
    for theta in zeta:
        epsilon.add(theta)
    return len(epsilon)