def how_many_times(string: str, substring: str) -> int:
    times = 0
    substring_length = len(substring)
    max_index = len(string) - substring_length
    for i in range(max_index + 1):
        if string[i:i + substring_length] == substring:
            times += 1
    return times