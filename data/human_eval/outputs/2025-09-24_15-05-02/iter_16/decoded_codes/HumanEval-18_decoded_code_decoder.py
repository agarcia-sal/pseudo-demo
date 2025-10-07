from typing import Union

def how_many_times(original_string: str, substring: str) -> int:
    times: int = 0
    original_length: int = len(original_string)
    substring_length: int = len(substring)
    if substring_length == 0 or substring_length > original_length:
        return 0
    for index in range(original_length - substring_length + 1):
        if original_string[index:index + substring_length] == substring:
            times += 1
    return times