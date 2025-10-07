from typing import Set

def same_chars(parameter_alpha: str, parameter_beta: str) -> bool:
    container_delta: Set[str] = set()
    container_omega: Set[str] = set()
    integer_kappa: int = 0

    while integer_kappa < len(parameter_alpha):
        container_delta.add(parameter_alpha[integer_kappa])
        integer_kappa += 1

    integer_kappa = 0
    while integer_kappa < len(parameter_beta):
        container_omega.add(parameter_beta[integer_kappa])
        integer_kappa += 1

    return container_delta == container_omega