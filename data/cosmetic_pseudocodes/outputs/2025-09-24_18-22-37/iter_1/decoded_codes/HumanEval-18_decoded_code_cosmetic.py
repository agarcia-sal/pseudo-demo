def how_many_times(original_string: str, target_substring: str) -> int:
    occurrence_count: int = 0
    max_start_index: int = len(original_string) - len(target_substring)
    index: int = 0
    while index <= max_start_index:
        current_segment: str = original_string[index : index + len(target_substring)]
        if current_segment == target_substring:
            occurrence_count += 1
        index += 1
    return occurrence_count