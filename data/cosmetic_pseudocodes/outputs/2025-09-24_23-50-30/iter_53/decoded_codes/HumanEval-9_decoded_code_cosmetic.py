from typing import List, Optional

def rolling_max(param_1: List[int]) -> List[int]:
    var_1: Optional[int] = None
    var_2: List[int] = []
    var_3: int = 0

    while var_3 < len(param_1):
        if var_1 is None:
            var_1 = param_1[var_3]
        else:
            var_1 = var_1 if var_1 >= param_1[var_3] else param_1[var_3]
        var_2.append(var_1)
        var_3 += 1

    return var_2