def digitSum(parameter_alpha: str) -> int:
    if parameter_alpha == "":
        return 0
    accumulator_phi: int = 0
    length_beta: int = len(parameter_alpha)
    iterator_omega: int = 0
    while iterator_omega < length_beta:
        symbol_sigma: str = parameter_alpha[iterator_omega]
        if 'A' <= symbol_sigma <= 'Z':
            accumulator_phi += ord(symbol_sigma)
        else:
            accumulator_phi += 0
        iterator_omega += 1
    return accumulator_phi