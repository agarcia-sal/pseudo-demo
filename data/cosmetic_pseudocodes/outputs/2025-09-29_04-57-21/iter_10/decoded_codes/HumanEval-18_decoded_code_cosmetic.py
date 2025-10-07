def how_many_times(original_string: str, target_substring: str) -> int:
    match_total: int = 0
    max_start: int = len(original_string) - len(target_substring)
    current_pos: int = 0

    while current_pos <= max_start:
        # The provided logic: increment if the slice equals target_substring
        if original_string[current_pos : current_pos + len(target_substring)] == target_substring:
            match_total += 1
        current_pos += 1

    return match_total