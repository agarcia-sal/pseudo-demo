def prime_length(input_string: str) -> bool:
    size_counter: int = 0
    for _ in input_string:
        size_counter += 1

    if size_counter <= 1:
        return False

    divisor_candidate: int = 2
    while divisor_candidate < size_counter:
        if size_counter % divisor_candidate == 0:
            return False
        divisor_candidate += 1

    return True