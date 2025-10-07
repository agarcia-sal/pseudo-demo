from typing import Union


def how_many_times(string: str, substring: str) -> int:
    if not isinstance(string, str) or not isinstance(substring, str):
        raise ValueError("Both 'string' and 'substring' must be of type str.")
    substring_length: int = len(substring)
    string_length: int = len(string)
    if substring_length == 0 or substring_length > string_length:
        return 0
    times: int = 0
    for index in range(string_length - substring_length + 1):
        if string[index : index + substring_length] == substring:
            times += 1
    return times