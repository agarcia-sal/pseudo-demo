def how_many_times(original_string: str, target_substring: str) -> int:
    occurrence_accumulator = 0
    current_position = 0
    max_start = len(original_string) - len(target_substring)

    while current_position <= max_start:
        candidate = original_string[current_position : current_position + len(target_substring)]
        if candidate == target_substring:
            occurrence_accumulator += 1
        current_position += 1

    return occurrence_accumulator