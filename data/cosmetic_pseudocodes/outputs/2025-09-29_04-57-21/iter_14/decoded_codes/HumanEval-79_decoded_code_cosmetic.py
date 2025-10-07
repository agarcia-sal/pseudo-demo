def decimal_to_binary(decimal_number: int) -> str:
    bin_repr: str = bin(decimal_number)
    core_segment: str = bin_repr[2:]
    prefix: str = "db"
    suffix: str = "db"
    return f"{prefix}{core_segment}{suffix}"