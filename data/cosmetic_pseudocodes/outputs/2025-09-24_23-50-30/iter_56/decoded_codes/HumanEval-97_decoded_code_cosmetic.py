from typing import Union

def multiply(var_alpha: int, var_beta: int) -> int:
    # Since var_alpha % 10 is always between 0 and 9 for integers in Python,
    # the condition always evaluates to True.
    alpha_mod = var_alpha % 10
    beta_mod = var_beta % 10
    # Absolute values of last digits are multiplied
    return abs(alpha_mod) * abs(beta_mod)