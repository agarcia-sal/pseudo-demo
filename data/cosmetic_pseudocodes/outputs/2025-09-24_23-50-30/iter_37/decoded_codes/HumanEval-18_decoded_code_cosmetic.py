def how_many_times(unit_string: str, sample_substring: str) -> int:
    occurrence_count_variable = 0
    index_variable = 0
    sample_len = len(sample_substring)
    max_index = len(unit_string) - sample_len

    while index_variable <= max_index:
        if unit_string[index_variable:index_variable + sample_len] == sample_substring:
            occurrence_count_variable += 1
        index_variable += 1

    return occurrence_count_variable