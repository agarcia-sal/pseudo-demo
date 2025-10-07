def is_prime(input_value: int) -> bool:
    threshold: int = 2
    if input_value < threshold:
        return False
    else:
        boundary_limit: int = input_value - 2
        index: int = 2
        while index <= boundary_limit:
            remainder: int = input_value % index
            if remainder == 0:
                return False
            index += 1
    return True