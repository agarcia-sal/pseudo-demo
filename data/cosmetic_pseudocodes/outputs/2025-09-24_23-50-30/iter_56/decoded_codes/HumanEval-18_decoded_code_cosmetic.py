def how_many_times(delta_string: str, omega_string: str) -> int:
    count_accum: int = 0
    idx: int = 0
    max_start: int = len(delta_string) - len(omega_string)
    while idx <= max_start:
        if delta_string[idx:idx + len(omega_string)] == omega_string:
            count_accum += 1
        idx += 1
    return count_accum