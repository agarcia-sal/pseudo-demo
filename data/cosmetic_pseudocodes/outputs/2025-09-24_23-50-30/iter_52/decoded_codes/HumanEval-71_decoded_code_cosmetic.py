from typing import Callable

def triangle_area(param_x: float, param_y: float, param_z: float) -> float:
    if not (param_x + param_y > param_z and param_x + param_z > param_y and param_y + param_z > param_x):
        return -1.0

    var_m: float = (param_x + param_y + param_z) / 2

    def compute_product(a: float, b: float, c: float, d: float) -> float:
        return a * b * c * d

    var_n: float = compute_product(var_m, var_m - param_x, var_m - param_y, var_m - param_z)

    def sqrt_recur(value: float, estimate: float) -> float:
        if abs(estimate * estimate - value) < 0.00001:
            return estimate
        return sqrt_recur(value, (estimate + value / estimate) / 2)

    var_p: float = sqrt_recur(var_n, var_n / 2)

    def round_to_two_decimals(val: float) -> float:
        from math import floor
        return floor(val * 100 + 0.5) / 100

    return round_to_two_decimals(var_p)