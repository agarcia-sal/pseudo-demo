def how_many_times(original_string: str, target_substring: str) -> int:
    count_occurrences = 0
    max_start = len(original_string) - len(target_substring)
    i = 0
    while i <= max_start:
        current_slice = original_string[i : i + len(target_substring)]
        if current_slice == target_substring:
            count_occurrences += 1
        i += 1
    return count_occurrences