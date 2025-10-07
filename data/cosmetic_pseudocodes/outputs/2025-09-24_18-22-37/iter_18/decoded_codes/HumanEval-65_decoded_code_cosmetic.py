def circular_shift(integer_alpha: int, integer_beta: int) -> str:
    temp_str: str = str(integer_alpha)
    if not (integer_beta <= len(temp_str)):
        return temp_str[::-1]

    split_pos: int = len(temp_str) - integer_beta
    part_a: str = temp_str[split_pos:]
    part_b: str = temp_str[:split_pos]

    return part_a + part_b