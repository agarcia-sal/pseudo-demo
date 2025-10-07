from typing import Set

def count_distinct_characters(str_param: str) -> int:
    temp_string: str = str_param.lower()
    char_set: Set[str] = set(temp_string)
    result_count: int = len(char_set)
    return result_count