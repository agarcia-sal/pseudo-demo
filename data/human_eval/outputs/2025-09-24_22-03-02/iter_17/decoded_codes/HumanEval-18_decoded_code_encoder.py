def how_many_times(string: str, substring: str) -> int:
    times = 0
    string_length = len(string)
    substring_length = len(substring)
    range_end = string_length - substring_length + 1
    for i in range(range_end):
        slice_ = string[i:i + substring_length]
        if slice_ == substring:
            times += 1
    return times