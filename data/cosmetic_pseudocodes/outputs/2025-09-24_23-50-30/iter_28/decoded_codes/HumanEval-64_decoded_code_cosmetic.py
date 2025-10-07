from typing import Set

def vowels_count(zeta: str) -> int:
    psi: Set[str] = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    def epsilon(beta: str, delta: int) -> int:
        if delta >= len(beta):
            return 0
        return (1 if beta[delta] in psi else 0) + epsilon(beta, delta + 1)

    alpha: int = epsilon(zeta, 0)

    if len(zeta) > 0 and (zeta[-1] == "y" or zeta[-1] == "Y"):
        alpha += 1

    return alpha