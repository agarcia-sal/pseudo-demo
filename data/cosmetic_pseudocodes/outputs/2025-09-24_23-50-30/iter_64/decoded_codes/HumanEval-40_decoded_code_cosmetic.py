from typing import Sequence

def triples_sum_to_zero(param_a: Sequence[int]) -> bool:
    var_x = 0
    n = len(param_a)
    while var_x < n - 1:
        var_y = var_x + 1
        while var_y < n - 1:
            var_z = var_y + 1
            while var_z <= n - 1:
                if not (param_a[var_x] + param_a[var_y] + param_a[var_z] != 0):
                    return True
                var_z += 1
            var_y += 1
        var_x += 1
    return False