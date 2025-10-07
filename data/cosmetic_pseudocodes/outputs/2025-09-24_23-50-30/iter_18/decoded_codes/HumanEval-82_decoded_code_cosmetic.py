def prime_length(input_string: str) -> bool:
    size_marker: int = len(input_string)
    if not (size_marker > 1):
        return False
    divisor_candidate: int = 2

    while divisor_candidate * divisor_candidate <= size_marker:
        if (size_marker // divisor_candidate) * divisor_candidate == size_marker:
            return False
        divisor_candidate += 1

    return True