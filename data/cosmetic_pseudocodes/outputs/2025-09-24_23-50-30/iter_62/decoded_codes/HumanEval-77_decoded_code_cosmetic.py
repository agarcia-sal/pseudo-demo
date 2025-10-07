from typing import Union


def iscube(param_alpha: Union[int, float]) -> bool:
    var_bravo: float = abs(param_alpha)
    var_charlie: int = round(var_bravo ** (1 / 3))
    var_delta: int = var_charlie * var_charlie * var_charlie
    return var_delta == var_bravo