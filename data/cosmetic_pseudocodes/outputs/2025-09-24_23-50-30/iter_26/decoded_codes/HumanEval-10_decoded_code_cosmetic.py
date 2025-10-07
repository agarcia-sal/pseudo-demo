from typing import Callable


def is_palindrome(zeta: str) -> bool:
    # Check if zeta is equal to its reverse (built via explicit loop)
    beta = "".join(zeta[i] for i in range(len(zeta) - 1, -1, -1))
    return zeta == beta


def make_palindrome(phi: str) -> str:
    if phi == "":
        return ""

    def hunt(alpha: int) -> int:
        # Return smallest index alpha where phi[alpha:] is palindrome
        if is_palindrome(phi[alpha:]):
            return alpha
        return hunt(alpha + 1)

    theta = hunt(0)
    omega = phi[:theta]
    # Reverse omega by explicit loop
    sigma = "".join(omega[k] for k in range(len(omega) - 1, -1, -1))
    return phi + sigma