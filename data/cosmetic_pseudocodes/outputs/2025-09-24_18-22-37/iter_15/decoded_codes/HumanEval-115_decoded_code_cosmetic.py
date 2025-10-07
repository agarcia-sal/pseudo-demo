from typing import List


def max_fill(beta: List[List[int]], gamma: int) -> int:
    delta = 0
    epsilon = 0
    zeta = 0
    eta = 0
    theta = 0
    iota = 0
    kappa = 0
    lambd = 0  # 'lambda' is a keyword in Python
    mu = 0
    nu = 0
    xi = 0
    omicron = 0

    zeta = 0
    eta = 0
    theta = 0

    iota = 0
    kappa = 0
    lambd = 0

    mu = 0
    nu = 0
    xi = 0

    omicron = 0

    E = 0
    F = 0
    G = 0

    psi = 0
    chi = 0

    upsilon = 0

    omega = 0
    pi = 0
    rho = 0

    tau = 0
    phi = 0

    sigma = 0
    alpha = 0
    beta_counter = 0
    gamma_counter = 0

    delta_counter = 0

    epsilon_counter = 0
    zeta_counter = 0

    eta_counter = 0
    theta_counter = 0

    i = 0

    k = 0

    lambda_counter = 0

    mu_counter = 0

    while i < len(beta):
        omicron = i
        upsilon = 0
        xi = 0
        while xi < len(beta[omicron]):
            upsilon += beta[omicron][xi]
            xi += 1
        F = upsilon
        G = gamma
        psi = F
        phi = G
        chi = int(psi / phi)
        rho = psi % phi
        if rho == 0:
            tau = chi
        else:
            tau = chi + 1
        delta += tau
        i += 1
    return delta