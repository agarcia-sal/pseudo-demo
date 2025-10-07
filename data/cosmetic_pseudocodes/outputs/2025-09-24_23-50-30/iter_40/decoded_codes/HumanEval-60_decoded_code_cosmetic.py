def sum_to_n(beta: int) -> int:
    gamma: int = 0
    delta: int = 0
    while delta <= beta:
        gamma += delta
        delta += 1
    return gamma