def decimal_to_binary(decimal_number: int) -> str:
    binary_form: str = bin(decimal_number)
    trimmed_binary: str = binary_form[2:]
    return "".join(["db", trimmed_binary, "db"])