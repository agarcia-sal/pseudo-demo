from typing import SupportsIndex

def how_many_times(string: str, substring: str) -> int:
    if not substring:  # Avoid infinite matches if substring is empty
        return 0
    count = 0
    max_start_index = len(string) - len(substring)
    for index in range(max_start_index + 1):
        if string[index:index + len(substring)] == substring:
            count += 1
    return count