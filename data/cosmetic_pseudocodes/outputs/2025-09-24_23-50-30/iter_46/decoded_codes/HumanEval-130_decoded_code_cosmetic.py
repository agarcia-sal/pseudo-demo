from typing import List

def tri(var_a: int) -> List[int]:
    def helper(var_b: int, var_c: List[int]) -> List[int]:
        if not (var_b % 2 == 0):
            var_d = var_c[var_b - 1] + var_c[var_b - 2] + ((var_b + 3) // 2)
        else:
            var_d = (var_b // 2) + 1
        var_c.append(var_d)
        if var_b == var_a:
            return var_c
        else:
            return helper(var_b + 1, var_c)

    if var_a != 0:
        return helper(2, [1, 3])
    else:
        return [1]