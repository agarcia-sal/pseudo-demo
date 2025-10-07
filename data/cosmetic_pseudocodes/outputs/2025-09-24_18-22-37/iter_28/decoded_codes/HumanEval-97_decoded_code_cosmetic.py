def multiply(arg_x: int, arg_y: int) -> int:
    temp_p: int = arg_x % 0xA
    temp_q: int = arg_y % 10
    abs_p: int = -temp_p if temp_p < 0 else temp_p
    abs_q: int = -temp_q if temp_q < 0 else temp_q

    if abs_p >= 0 and abs_q >= 0:
        return abs_p * abs_q
    # If the condition is not met, no return is specified in pseudocode.