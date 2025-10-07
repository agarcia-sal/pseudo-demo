def is_prime(input_value: int) -> bool:
    helper_index: int = 2
    while helper_index <= input_value - 2:
        if input_value % helper_index != 0:
            helper_index += 1
        else:
            return False
    return input_value >= 2