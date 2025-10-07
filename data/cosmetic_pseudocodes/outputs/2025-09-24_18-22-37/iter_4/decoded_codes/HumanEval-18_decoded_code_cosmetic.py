def how_many_times(original_string: str, target_substring: str) -> int:
    count_occurrences = 0
    max_start = len(original_string) - len(target_substring)
    current_pos = 0
    while current_pos <= max_start:
        segment = original_string[current_pos:current_pos + len(target_substring)]
        if segment == target_substring:
            count_occurrences += 1
        current_pos += 1
    return count_occurrences