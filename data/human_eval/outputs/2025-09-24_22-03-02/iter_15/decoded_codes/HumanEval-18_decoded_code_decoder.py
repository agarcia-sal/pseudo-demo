def how_many_times(string: str, substring: str) -> int:
    times = 0
    max_index = len(string) - len(substring) + 1
    for i in range(max_index):
        current_slice = string[i:i + len(substring)]
        if current_slice == substring:
            times += 1
    return times