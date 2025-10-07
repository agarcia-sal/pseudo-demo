def decimal_to_binary(num: int) -> str:
    bin_repr: str = bin(num)
    trimmed_bin: str = ""
    idx: int = 2
    while idx <= len(bin_repr):
        trimmed_bin += bin_repr[idx - 1]
        idx += 1
    result: str = "db" + trimmed_bin + "db"
    return result