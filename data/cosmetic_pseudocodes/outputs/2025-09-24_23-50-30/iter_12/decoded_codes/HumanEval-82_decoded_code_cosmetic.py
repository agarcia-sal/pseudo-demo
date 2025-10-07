def prime_length(input_string: str) -> bool:
    count: int = len(input_string)
    if count <= 1:
        return False
    index: int = 2
    while index < count:
        if count % index == 0:
            return False
        index += 1
    return True