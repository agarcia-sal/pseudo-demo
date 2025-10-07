def prime_length(input_string: str) -> bool:
    total_chars: int = len(input_string)
    if not (total_chars > 1):
        return False
    index: int = 2
    while index < total_chars:
        if total_chars % index == 0:
            return False
        index += 1
    return True