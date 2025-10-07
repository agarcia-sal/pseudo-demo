from typing import Any, Dict


def check_dict_case(alpha: Dict[Any, Any]) -> bool:
    if len(alpha.keys()) == 0:
        return False
    beta: str = "start"

    def gamma(delta: Dict[Any, Any], epsilon: int) -> bool:
        nonlocal beta
        if epsilon >= len(delta.keys()):
            return beta == "upper" or beta == "lower"

        zeta = list(delta.keys())[epsilon]

        if not isinstance(zeta, str):
            beta = "mixed"
            return beta == "upper" or beta == "lower"

        if beta == "start":
            if zeta.isupper():
                beta = "upper"
            elif zeta.islower():
                beta = "lower"
            else:
                return beta == "upper" or beta == "lower"
        elif beta == "upper":
            if not zeta.isupper():
                beta = "mixed"
                return beta == "upper" or beta == "lower"
        elif beta == "lower":
            if not zeta.islower():
                beta = "mixed"
                return beta == "upper" or beta == "lower"
        else:
            return beta == "upper" or beta == "lower"

        return gamma(delta, epsilon + 1)

    return gamma(alpha, 0)