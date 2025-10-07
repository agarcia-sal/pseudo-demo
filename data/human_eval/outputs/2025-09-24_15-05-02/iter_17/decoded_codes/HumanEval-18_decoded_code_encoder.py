from typing import Union

def how_many_times(string: str, substring: str) -> int:
    times: int = 0
    substring_length: int = len(substring)
    max_start_index: int = len(string) - substring_length + 1
    for i in range(max_start_index):
        if string[i:i + substring_length] == substring:
            times += 1
    return times