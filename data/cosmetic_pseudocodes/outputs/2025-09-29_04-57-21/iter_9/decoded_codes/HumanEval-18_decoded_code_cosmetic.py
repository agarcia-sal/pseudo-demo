def how_many_times(original_string: str, target_substring: str) -> int:
    total_occurrences: int = 0
    max_start: int = len(original_string) - len(target_substring)
    current_pos: int = 0

    while current_pos <= max_start:
        if original_string[current_pos:current_pos + len(target_substring)] == target_substring:
            total_occurrences += 1
        current_pos += 1

    return total_occurrences