def prime_length(alphanumeric_input: str) -> bool:
    alpha_count: int = len(alphanumeric_input)
    if alpha_count <= 1:
        return False
    index_tracker: int = 2
    while index_tracker < alpha_count:
        if alpha_count % index_tracker == 0:
            return False
        index_tracker += 1
    return True