def decimal_to_binary(x: int) -> str:
    value = bin(x)
    trimmed = value[2:]
    prefix = "db"
    suffix = "db"
    return prefix + trimmed + suffix