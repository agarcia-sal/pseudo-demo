def count_distinct_characters(gamma: str) -> int:
    delta: set[str] = set()
    for zeta in gamma:
        theta = zeta.lower()
        if theta not in delta:
            delta.add(theta)
    epsilon = len(delta)
    return epsilon