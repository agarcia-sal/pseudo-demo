def how_many_times(original_string: str, target_substring: str) -> int:
    occurrence_count: int = 0
    max_start: int = len(original_string) - len(target_substring)
    for index in range(max_start + 1):
        candidate: str = original_string[index : index + len(target_substring)]
        if candidate == target_substring:
            occurrence_count += 1
    return occurrence_count