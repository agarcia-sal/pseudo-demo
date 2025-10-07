from typing import Literal

def how_many_times(string: str, substring: str) -> int:
    times: int = 0
    substr_len: int = len(substring)
    max_start_index: int = len(string) - substr_len
    if substr_len == 0 or max_start_index < 0:
        return 0
    for index in range(max_start_index + 1):
        if string[index:index + substr_len] == substring:
            times += 1
    return times