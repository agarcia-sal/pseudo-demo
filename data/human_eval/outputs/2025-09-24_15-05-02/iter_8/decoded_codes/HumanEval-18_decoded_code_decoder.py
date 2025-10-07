from typing import Sequence

def how_many_times(string: str, substring: str) -> int:
    times: int = 0
    substring_length: int = len(substring)
    limit: int = len(string) - substring_length
    for index in range(limit + 1):
        if string[index:index + substring_length] == substring:
            times += 1
    return times