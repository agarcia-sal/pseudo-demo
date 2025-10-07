from typing import Set

def count_distinct_characters(delta: str) -> int:
    theta: str = ""
    for eps in range(1, len(delta) + 1):
        phi: str = delta[eps - 1].lower()  # Adjust 1-based index to 0-based
        theta += phi
    omega: Set[str] = set(theta)
    sigma: int = len(omega)
    return sigma