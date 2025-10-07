def how_many_times(original_string: str, target_substring: str) -> int:
    occurrence_count: int = 0
    max_start_index = len(original_string) - len(target_substring)
    if max_start_index < 0:
        return 0
    for index in range(max_start_index + 1):
        if original_string[index:index + len(target_substring)] == target_substring:
            occurrence_count += 1
    return occurrence_count