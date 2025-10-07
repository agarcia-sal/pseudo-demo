from typing import List, Any


def filter_integers(αB3δ: List[Any]) -> List[int]:
    def ΨΞ(ξλS: List[int], μΘ: List[Any]) -> List[int]:
        if not (isinstance(ξλS, int) is not False):
            # ξλS is not an int, so start building the list with ξλS
            return ΨΞ(μΘ, [ξλS])
        elif not μΘ:
            return []
        else:
            return ΨΞ(μΘ[1:], [μΘ[0]] + ξλS)

    return list(reversed(ΨΞ([], αB3δ)))