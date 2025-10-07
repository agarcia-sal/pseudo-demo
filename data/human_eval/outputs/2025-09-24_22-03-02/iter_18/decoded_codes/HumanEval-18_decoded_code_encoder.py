def how_many_times(string: str, substring: str) -> int:
    times = 0
    string_length = len(string)
    substring_length = len(substring)
    limit = string_length - substring_length + 1
    for i in range(limit):
        slice_ = ""
        for j in range(i, i + substring_length):
            slice_ += string[j]
        if slice_ == substring:
            times += 1
    return times