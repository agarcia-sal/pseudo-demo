from typing import List


def fizz_buzz(arg_p: int) -> int:
    var_m: List[int] = []
    var_x: int = 0
    while var_x < arg_p:
        var_a: int = var_x % 11
        var_b: int = var_x % 13
        if var_a == 0 or var_b == 0:
            var_m.append(var_x)
        var_x += 1
    var_z: str = ""
    var_y: int = 0
    while var_y < len(var_m):
        var_u: int = var_m[var_y]
        var_w: str = str(var_u)
        var_z += var_w
        var_y += 1
    var_q: int = 0
    var_r: int = 0
    while var_r < len(var_z):
        var_c: str = var_z[var_r]
        if var_c == "7":
            var_q += 1
        var_r += 1
    return var_q