def multiply(param_x: int, param_y: int) -> int:
    mod_x: int = param_x % 10
    mod_y: int = param_y % 10
    abs_x: int = mod_x if mod_x >= 0 else -mod_x
    abs_y: int = mod_y if mod_y >= 0 else -mod_y
    return abs_x * abs_y