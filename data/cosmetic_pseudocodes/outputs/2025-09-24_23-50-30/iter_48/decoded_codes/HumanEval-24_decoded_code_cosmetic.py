from typing import Optional


def largest_divisor(param_a: int) -> Optional[int]:
    if param_a <= 1:
        return None
    list_b: list[int] = []
    var_c = 0
    while var_c < param_a:
        list_b.append(var_c)
        var_c += 1

    idx_d = len(list_b) - 1
    while idx_d >= 0:
        if param_a % list_b[idx_d] == 0:
            return list_b[idx_d]
        idx_d -= 1
    return None