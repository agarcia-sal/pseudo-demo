def how_many_times(original_string: str, target_substring: str) -> int:
    occurrence_count: int = 0
    max_index: int = len(original_string) - len(target_substring)
    current_index: int = 0
    while current_index <= max_index:
        if target_substring == original_string[current_index : current_index + len(target_substring)]:
            occurrence_count += 1
        current_index += 1
    return occurrence_count