def decimal_to_binary(input_val: int) -> str:
    bin_representation: str = bin(input_val)
    trimmed_bin: str = bin_representation[1:]
    return "db" + trimmed_bin + "db"