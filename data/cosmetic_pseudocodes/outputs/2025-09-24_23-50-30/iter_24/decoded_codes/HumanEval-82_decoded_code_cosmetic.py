def prime_length(parameter_alpha: str) -> bool:
    length_beta: int = len(parameter_alpha)
    if length_beta <= 1:
        return False
    index_gamma: int = 2
    while index_gamma <= length_beta - 1:
        if length_beta % index_gamma == 0:
            return False
        index_gamma += 1
    return True