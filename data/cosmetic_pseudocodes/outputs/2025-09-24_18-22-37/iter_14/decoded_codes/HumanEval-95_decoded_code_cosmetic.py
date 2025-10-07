from typing import Any, Dict

def check_dict_case(omega: Dict[Any, Any]) -> bool:
    keys = list(omega.keys())
    if len(keys) == 0:
        return False

    alpha: str = "start"
    i: int = 0
    zeta: int = len(keys)
    while i < zeta:
        rho = keys[i]

        if not isinstance(rho, str):
            alpha = "mixed"
            break

        if alpha == "start":
            if rho == rho.upper():
                alpha = "upper"
            elif rho == rho.lower():
                alpha = "lower"
            else:
                break

        else:
            if (alpha == "upper" and rho != rho.upper()) or (alpha == "lower" and rho != rho.lower()):
                alpha = "mixed"
                break
            else:
                break

        i += 1

    return alpha == "upper" or alpha == "lower"