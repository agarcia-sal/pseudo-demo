def how_many_times(string: str, substring: str) -> int:
    times = 0
    str_len = len(string)
    sub_len = len(substring)
    for i in range(str_len - sub_len + 1):
        if string[i:i + sub_len] == substring:
            times += 1
    return times