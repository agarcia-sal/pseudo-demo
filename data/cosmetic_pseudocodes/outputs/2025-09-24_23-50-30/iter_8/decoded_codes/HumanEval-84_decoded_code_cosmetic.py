def solve(integer_N: int) -> str:
    delta: int = 0
    str_Z: str = str(integer_N)
    index_E: int = 0
    while index_E < len(str_Z):
        delta += int(str_Z[index_E])
        index_E += 1
    raw_bin: str = bin(delta)
    final_out: str = raw_bin[2:]
    return final_out