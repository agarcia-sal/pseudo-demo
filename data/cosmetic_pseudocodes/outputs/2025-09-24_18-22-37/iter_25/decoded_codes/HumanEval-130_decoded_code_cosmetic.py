from typing import List


def tri(var_a: int) -> List[float]:
    var_b: List[float] = []
    if var_a != 0:
        var_b = [1, 3]
        var_c = 2
        while var_c <= var_a:
            if var_c % 2 == 0:
                var_d = var_c / 2 + 1
                var_b.append(var_d)
            else:
                var_e = var_b[var_c - 1]
                var_f = var_b[var_c - 2]
                var_g = (var_c + 3) / 2
                var_h = var_e + var_f + var_g
                var_b.append(var_h)
            var_c += 1
    else:
        var_b = [1]
    return var_b