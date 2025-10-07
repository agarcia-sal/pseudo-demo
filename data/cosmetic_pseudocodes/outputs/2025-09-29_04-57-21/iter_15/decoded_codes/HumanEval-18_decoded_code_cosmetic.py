def how_many_times(original_string: str, target_substring: str) -> int:
    tally = 0
    upper_bound = len(original_string) - len(target_substring)
    iterator = 0

    while iterator <= upper_bound:
        segment = ""
        for position in range(len(target_substring)):
            segment += original_string[iterator + position]
        if segment == target_substring:
            tally += 1
        iterator += 1

    return tally