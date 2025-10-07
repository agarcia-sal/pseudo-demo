from typing import Any, Dict


def check_dict_case(jumble: Dict[Any, Any]) -> bool:
    if len(jumble.keys()) == 0:
        return False
    roman: str = "start"
    alpha_list = list(jumble.keys())
    beta = 0
    while beta < len(alpha_list):
        gamma = alpha_list[beta]
        if not isinstance(gamma, str):
            roman = "mixed"
            break
        if roman == "start":
            if gamma == gamma.upper():
                roman = "upper"
            elif gamma == gamma.lower():
                roman = "lower"
            else:
                break
        elif (roman == "upper" and gamma != gamma.upper()) or (roman == "lower" and gamma != gamma.lower()):
            roman = "mixed"
            break
        else:
            break
        beta += 1
    return roman == "upper" or roman == "lower"