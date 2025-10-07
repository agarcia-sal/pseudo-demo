def how_many_times(original_string: str, target_substring: str) -> int:
    tally = 0
    limit = len(original_string) - len(target_substring)
    pointer = 0

    while pointer <= limit:
        if original_string[pointer : pointer + len(target_substring)] == target_substring:
            tally += 1
        pointer += 1

    return tally