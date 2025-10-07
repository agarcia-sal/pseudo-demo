def decimal_to_binary(num: int) -> str:
    bin_representation: str = bin(num)
    middle_section: str = bin_representation[2:-1]  # remove '0b' prefix and last char
    prefix: str = "db"
    suffix: str = "db"
    return f"{prefix}{middle_section}{suffix}"