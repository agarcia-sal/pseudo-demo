from typing import Final

def how_many_times(string: str, substring: str) -> int:
    times: int = 0
    max_start_index: Final = len(string) - len(substring)
    if max_start_index < 0:
        return 0
    for index in range(max_start_index + 1):
        if string[index:index + len(substring)] == substring:
            times += 1
    return times