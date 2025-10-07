def decimal_to_binary(param_alpha: int) -> str:
    temp_beta: str = bin(param_alpha)
    temp_gamma: str = temp_beta[2:]
    return "db" + temp_gamma + "db"