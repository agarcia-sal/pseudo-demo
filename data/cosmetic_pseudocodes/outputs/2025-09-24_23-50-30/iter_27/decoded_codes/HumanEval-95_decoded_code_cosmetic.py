from typing import Any, Dict


def check_dict_case(alpha: Dict[Any, Any]) -> bool:
    if len(alpha.keys()) == 0:
        return False

    beta: str = "start"
    gammaList = list(alpha.keys())
    delta = 0

    while delta < len(gammaList):
        epsilon = gammaList[delta]

        if not isinstance(epsilon, str):
            beta = "mixed"
            break

        if beta == "start":
            if epsilon.upper() == epsilon:
                beta = "upper"
            elif epsilon.lower() == epsilon:
                beta = "lower"
            else:
                break

        elif beta == "upper":
            if epsilon.upper() != epsilon:
                beta = "mixed"
                break

        elif beta == "lower":
            if epsilon.lower() != epsilon:
                beta = "mixed"
                break

        delta += 1

    return beta == "upper" or beta == "lower"