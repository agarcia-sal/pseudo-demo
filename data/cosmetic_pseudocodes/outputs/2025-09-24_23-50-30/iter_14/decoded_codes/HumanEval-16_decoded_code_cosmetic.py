from typing import List

def count_distinct_characters(str_param: str) -> int:
    lowered_chars: List[str] = [ch.lower() for ch in str_param]
    unique_chars: dict[str, bool] = {elem: True for elem in lowered_chars}
    return len(unique_chars)