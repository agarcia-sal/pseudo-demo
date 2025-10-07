def how_many_times(string: str, substring: str) -> int:
    times: int = 0
    str_len = len(string)
    sub_len = len(substring)
    if sub_len == 0 or sub_len > str_len:
        return 0
    for index in range(str_len - sub_len + 1):
        if string[index:index + sub_len] == substring:
            times += 1
    return times