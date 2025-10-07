def prime_length(input_string: str) -> bool:
    size_counter: int = len(input_string)
    if size_counter == 0 or size_counter == 1:
        return False
    index: int = 2
    while index < size_counter:
        if size_counter % index == 0:
            return False
        index += 1
    return True