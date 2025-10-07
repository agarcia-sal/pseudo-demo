def prime_length(input_string: str) -> bool:
    size_tracker: int = len(input_string)
    if size_tracker == 0 or size_tracker == 1:
        return False
    divisor_counter: int = 2
    while divisor_counter < size_tracker:
        if size_tracker % divisor_counter == 0:
            return False
        divisor_counter += 1
    return True