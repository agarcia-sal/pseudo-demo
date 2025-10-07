def how_many_times(string: str, substring: str) -> int:
    times = 0
    substr_len = len(substring)
    max_index = len(string) - substr_len
    if substr_len == 0 or max_index < 0:
        return 0
    for i in range(max_index + 1):
        if string[i:i + substr_len] == substring:
            times += 1
    return times