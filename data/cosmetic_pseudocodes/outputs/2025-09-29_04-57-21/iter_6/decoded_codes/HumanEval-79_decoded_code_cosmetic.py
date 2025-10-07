def decimal_to_binary(decimal_number: int) -> str:
    binary_rep: str = bin(decimal_number)
    sliced_binary: str = binary_rep[2:]
    return "db" + sliced_binary + "db"