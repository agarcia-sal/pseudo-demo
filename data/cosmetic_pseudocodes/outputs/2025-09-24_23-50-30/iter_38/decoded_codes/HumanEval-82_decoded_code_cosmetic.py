def prime_length(input_string: str) -> bool:
    delta: int = len(input_string)
    if not (delta > 1):
        return False
    index: int = 2
    while index < delta:
        if delta % index == 0:
            return False
        index += 1
    return True