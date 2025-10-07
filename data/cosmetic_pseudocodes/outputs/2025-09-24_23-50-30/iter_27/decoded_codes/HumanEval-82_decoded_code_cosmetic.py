def prime_length(str_param: str) -> bool:
    length_var: int = len(str_param)
    if length_var == 0 or length_var == 1:
        return False
    index_var: int = 2
    while index_var <= length_var - 1:
        if length_var % index_var == 0:
            return False
        index_var += 1
    return True