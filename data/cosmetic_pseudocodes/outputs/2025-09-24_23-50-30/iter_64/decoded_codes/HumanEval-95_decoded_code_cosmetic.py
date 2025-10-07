from typing import Any, Dict, List, Optional


def check_dict_case(alpha: Dict[Any, Any]) -> bool:
    if len(alpha.keys()) == 0:
        return False  # 0 <> 0 is False

    beta: str = "start"
    gamma_list: List[Any] = list(alpha.keys())

    def delta(epsilon: Optional[Any], zeta: int) -> bool:
        nonlocal beta
        if zeta >= len(gamma_list):
            return beta == "upper" or beta == "lower"

        eta = gamma_list[zeta]

        if not isinstance(eta, str):
            beta = "mixed"
            return beta == "upper" or beta == "lower"

        if beta == "start":
            if eta.isupper():
                beta = "upper"
                return delta(epsilon, zeta + 1)
            elif eta.islower():
                beta = "lower"
                return delta(epsilon, zeta + 1)
            else:
                return beta == "upper" or beta == "lower"
        elif (beta == "upper" and not eta.isupper()) or (beta == "lower" and not eta.islower()):
            beta = "mixed"
            return beta == "upper" or beta == "lower"
        else:
            return beta == "upper" or beta == "lower"

    return delta(None, 0)