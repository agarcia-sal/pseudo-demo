def how_many_times(string: str, substring: str) -> int:
    times = 0
    substr_len = len(substring)
    max_start = len(string) - substr_len

    for i in range(max_start + 1):
        if string[i:i + substr_len] == substring:
            times += 1

    return times