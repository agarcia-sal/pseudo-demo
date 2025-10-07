def how_many_times(original_string: str, target_substring: str) -> int:
    match_total: int = 0
    current_position: int = 0
    target_len: int = len(target_substring)
    max_start: int = len(original_string) - target_len

    while current_position <= max_start:
        if original_string[current_position:current_position + target_len] == target_substring:
            match_total += 1
        current_position += 1

    return match_total