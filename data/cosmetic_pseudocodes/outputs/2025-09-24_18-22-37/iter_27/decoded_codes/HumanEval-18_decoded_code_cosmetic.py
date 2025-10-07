def how_many_times(original_string: str, target_substring: str) -> int:
    count_accumulator: int = 0
    upper_limit: int = len(original_string) - len(target_substring)
    iterator_i: int = 0
    while iterator_i <= upper_limit:
        current_piece = original_string[iterator_i : iterator_i + len(target_substring)]
        if current_piece == target_substring:
            count_accumulator += 1
        iterator_i += 1
    return count_accumulator