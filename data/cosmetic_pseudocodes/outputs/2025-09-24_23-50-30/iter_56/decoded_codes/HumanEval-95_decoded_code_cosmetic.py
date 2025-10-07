from typing import Any, Mapping

def check_dict_case(rho: Mapping[Any, Any]) -> bool:
    if not len(rho):
        return False
    sigma: str = "start"
    for xi in rho.keys():
        if not isinstance(xi, str):
            sigma = "mixed"
            break
        if sigma == "start":
            if xi.isupper():
                sigma = "upper"
            elif xi.islower():
                sigma = "lower"
            else:
                break
        elif sigma == "upper":
            if not xi.isupper():
                sigma = "mixed"
                break
            else:
                break
        elif sigma == "lower":
            if not xi.islower():
                sigma = "mixed"
                break
            else:
                break
    return sigma == "upper" or sigma == "lower"