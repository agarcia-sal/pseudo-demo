from typing import List


def f(integer_n: int) -> List[int]:
    result: List[int] = []

    # First block: if ψ != 0 (assuming ψ == integer_n)
    if integer_n != 0:
        beta_phi_0 = 1
        omega = 1
        while omega <= integer_n:
            beta_phi_0 *= omega
            omega += 1
        result.insert(0, beta_phi_0)

    # Second block: if ψ != 0
    if integer_n != 0:
        beta_chi = 0
        omega = 1
        while omega <= integer_n:
            beta_chi += omega
            omega += 1
        result.insert(0, beta_chi)

    omega_psi = 1
    while omega_psi <= integer_n:
        if omega_psi % 2 == 0:
            o_function(omega_psi, result)
        else:
            diamond_function(omega_psi, result)
        omega_psi += 1

    result.reverse()
    return result


def o_function(xi_1: int, delta_omega: List[int]) -> None:
    phi = 1
    kappa = 1
    while kappa <= xi_1:
        phi *= kappa
        kappa += 1
    delta_omega.insert(0, phi)


def diamond_function(xi_1: int, delta_omega: List[int]) -> None:
    zeta = 0
    tau = 1
    while tau <= xi_1:
        zeta += tau
        tau += 1
    delta_omega.insert(0, zeta)