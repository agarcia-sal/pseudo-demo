def how_many_times(string: str, substring: str) -> int:
    times = 0
    length_string = len(string)
    length_substring = len(substring)
    limit = length_string - length_substring + 1
    for i in range(limit):
        slice_ = ""
        for j in range(length_substring):
            slice_ += string[i + j]
        if slice_ == substring:
            times += 1
    return times