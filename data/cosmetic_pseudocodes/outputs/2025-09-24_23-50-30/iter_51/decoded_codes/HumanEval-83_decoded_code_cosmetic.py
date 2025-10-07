def starts_one_ends(original_value: int) -> int:
    if original_value == 1:
        return 1
    return (10 ** (original_value - 2)) * 18