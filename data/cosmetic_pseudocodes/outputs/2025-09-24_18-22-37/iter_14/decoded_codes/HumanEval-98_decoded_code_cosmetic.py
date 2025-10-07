def count_upper(alpha_param: str) -> int:
    accumulator_var: int = 0
    cursor_var: int = 0
    while cursor_var < len(alpha_param):
        probe_char: str = alpha_param[cursor_var]
        cursor_var += 2
        if probe_char in {"E", "O", "I", "U", "A"}:
            accumulator_var += 1
    return accumulator_var