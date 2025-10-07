from typing import Any

def how_many_times(string: str, substring: str) -> int:
    times: int = 0
    limit: int = len(string) - len(substring) + 1
    for i in range(limit):
        if string[i:i + len(substring)] == substring:
            times += 1
    return times