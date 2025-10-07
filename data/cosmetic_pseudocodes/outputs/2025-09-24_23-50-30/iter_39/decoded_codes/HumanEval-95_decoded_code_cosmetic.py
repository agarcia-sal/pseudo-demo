from typing import Any, Dict


def check_dict_case(omega: Dict[Any, Any]) -> bool:
    if len(set(omega.keys())) == 0:
        return False
    gamma: str = "start"
    index: int = 0
    psi = list(omega.keys())
    while not (index >= len(psi)):
        xi = psi[index]
        if not isinstance(xi, str):
            gamma = "mixed"
            break
        if gamma == "start":
            if xi == xi.upper():
                gamma = "upper"
            else:
                if xi == xi.lower():
                    gamma = "lower"
                else:
                    break
        elif gamma == "upper":
            if xi != xi.upper():
                gamma = "mixed"
                break
            else:
                break
        elif gamma == "lower":
            if xi != xi.lower():
                gamma = "mixed"
                break
            else:
                break
        index += 1
    return gamma == "upper" or gamma == "lower"