def decimal_to_binary(decVal: int) -> str:
    prefix_suffix: str = "db"
    binStr: str = bin(decVal)
    slicedBin: str = binStr[2:]  # Remove '0b' prefix
    result: str = f"{prefix_suffix}{slicedBin}{prefix_suffix}"
    return result