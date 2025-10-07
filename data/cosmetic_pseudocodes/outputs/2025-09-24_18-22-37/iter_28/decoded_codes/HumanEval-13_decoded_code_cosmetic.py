def greatest_common_divisor(alpha: int, beta: int) -> int:
    isRunning: bool = True
    while isRunning:
        if beta == 0:
            isRunning = False
            continue
        hold_var: int = beta
        mod_result: int = alpha % beta
        beta = mod_result
        alpha = hold_var
    return alpha