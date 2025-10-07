def how_many_times(original_string: str, target_substring: str) -> int:
    count_occurrences = 0
    position = 0
    max_start = len(original_string) - len(target_substring)
    while position <= max_start:
        if original_string[position : position + len(target_substring)] == target_substring:
            count_occurrences += 1
        position += 1
    return count_occurrences