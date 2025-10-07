def decimal_to_binary(kappa: int) -> str:
    binary_form: str = bin(kappa)
    midway_string: str = binary_form[2:]
    return "db" + midway_string + "db"