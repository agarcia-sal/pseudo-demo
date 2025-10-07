from typing import Union

def how_many_times(string: str, substring: str) -> int:
    times = 0
    limit = len(string) - len(substring) + 1
    for i in range(limit):
        if string[i:i + len(substring)] == substring:
            times += 1
    return times