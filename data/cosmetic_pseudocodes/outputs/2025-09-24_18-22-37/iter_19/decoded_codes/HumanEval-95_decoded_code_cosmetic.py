from typing import Dict, Any


def check_dict_case(zeta: Dict[Any, Any]) -> bool:
    if not zeta.keys():
        return False

    alpha: str = "start"
    omega = list(zeta.keys())
    kappa: int = 0

    while kappa < len(omega):
        epsilon = omega[kappa]

        if not isinstance(epsilon, str):
            alpha = "mixed"
            break

        if alpha == "start":
            if epsilon.isupper():
                alpha = "upper"
            elif epsilon.islower():
                alpha = "lower"
            else:
                break

        elif alpha == "upper":
            if not epsilon.isupper():
                alpha = "mixed"
                break
            else:
                break

        elif alpha == "lower":
            if not epsilon.islower():
                alpha = "mixed"
                break
            else:
                break

        kappa += 1

    return alpha == "upper" or alpha == "lower"