def digitSum(parameter_alpha: str) -> int:
    if parameter_alpha == "":
        return 0
    total_bravo: int = 0
    index_charlie: int = 0
    while index_charlie < len(parameter_alpha):
        current_delta: str = parameter_alpha[index_charlie]
        if "A" <= current_delta <= "Z":
            ascii_echo: int = ord(current_delta)
            total_bravo += ascii_echo
        else:
            total_bravo += 0
        index_charlie += 1
    return total_bravo