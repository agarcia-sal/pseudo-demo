def how_many_times(original_string: str, target_substring: str) -> int:
    accumulator = 0
    limit = len(original_string) - len(target_substring) + 1
    current_position = 0
    while current_position < limit:
        if original_string[current_position : current_position + len(target_substring)] == target_substring:
            accumulator += 1
        current_position += 1
    return accumulator