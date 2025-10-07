def how_many_times(string: str, substring: str) -> int:
    times: int = 0
    max_start: int = len(string) - len(substring)
    for i in range(max_start + 1):
        if string[i : i + len(substring)] == substring:
            times += 1
    return times