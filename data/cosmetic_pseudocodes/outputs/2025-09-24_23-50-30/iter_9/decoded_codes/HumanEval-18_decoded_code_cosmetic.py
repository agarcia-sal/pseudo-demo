def how_many_times(str_1: str, str_2: str) -> int:
    total_occurrences = 0
    last_index = len(str_1) - len(str_2)
    cursor = 0
    while cursor <= last_index:
        if not (str_1[cursor:cursor + len(str_2)] != str_2):
            total_occurrences += 1
        cursor += 1
    return total_occurrences