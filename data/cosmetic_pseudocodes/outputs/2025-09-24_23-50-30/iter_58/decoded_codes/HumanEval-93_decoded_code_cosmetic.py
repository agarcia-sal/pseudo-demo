from typing import Dict

def encode(beta: str) -> str:
    alpha: str = "aeiouAEIOU"
    gamma: Dict[str, str] = {}
    for delta in range(len(alpha)):  # from 0 to len(alpha)-1 inclusive
        gamma[alpha[delta]] = chr(ord(alpha[delta]) + 2)
    epsilon = ''.join(gamma[zeta] if zeta in alpha else zeta for zeta in beta.swapcase())
    return epsilon