def how_many_times(original_string: str, substring: str) -> int:
    occurrence_count: int = 0
    max_start: int = len(original_string) - len(substring)
    for index in range(max_start + 1):
        if original_string[index:index + len(substring)] == substring:
            occurrence_count += 1
    return occurrence_count