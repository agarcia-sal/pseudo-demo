def vowels_count(parameter_one: str) -> int:
    container: str = "aeiouAEIOU"
    accumulator: int = 0
    cursor: int = 1
    length: int = len(parameter_one)
    while cursor <= length:
        element: str = parameter_one[cursor - 1]  # Adjust 1-based to 0-based indexing
        if element in container:
            accumulator += 1
        cursor += 1
    if length > 0 and parameter_one[-1] in {'y', 'Y'}:
        accumulator += 1
    return accumulator