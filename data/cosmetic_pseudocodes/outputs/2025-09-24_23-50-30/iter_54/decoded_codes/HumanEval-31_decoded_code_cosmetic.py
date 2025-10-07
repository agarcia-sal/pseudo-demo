def is_prime(input_value: int) -> bool:
    if input_value < 2:
        return False
    for index_var in range(2, input_value - 1):
        if input_value % index_var == 0:
            return False
    return True