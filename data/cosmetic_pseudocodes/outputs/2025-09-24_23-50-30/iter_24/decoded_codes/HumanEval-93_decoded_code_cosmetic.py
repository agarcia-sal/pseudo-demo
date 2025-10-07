from typing import Dict


def encode(theta: str) -> str:
    lambda_vowels: str = "AEIOUaeiou"
    mu: Dict[str, str] = {}

    for k in range(len(lambda_vowels)):
        alpha = lambda_vowels[k]
        mu[alpha] = chr(ord(alpha) + 2)

    rho = []
    for sigma in theta:
        if sigma.isupper():
            rho.append(sigma.lower())
        elif sigma.islower():
            rho.append(sigma.upper())
        else:
            rho.append(sigma)
    rho_str = ''.join(rho)

    phi = []
    i = 0
    while i < len(rho_str):
        zeta = rho_str[i]
        if zeta not in lambda_vowels:
            phi.append(zeta)
            i += 1
            continue
        phi.append(mu[zeta])
        i += 1

    return ''.join(phi)