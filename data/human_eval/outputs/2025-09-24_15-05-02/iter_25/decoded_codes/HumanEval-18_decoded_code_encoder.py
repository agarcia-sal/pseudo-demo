from typing import List

def how_many_times(string: str, substring: str) -> int:
    times: int = 0
    substr_len: int = len(substring)
    if substr_len == 0 or substr_len > len(string):
        return 0
    for index in range(len(string) - substr_len + 1):
        if string[index:index + substr_len] == substring:
            times += 1
    return times