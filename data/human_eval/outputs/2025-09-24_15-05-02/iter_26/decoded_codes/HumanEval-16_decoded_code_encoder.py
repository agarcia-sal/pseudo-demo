from typing import Union

def count_distinct_characters(string: Union[str, bytes]) -> int:
    lowered_string = string.lower() if isinstance(string, str) else string.decode().lower()
    return len(set(lowered_string))