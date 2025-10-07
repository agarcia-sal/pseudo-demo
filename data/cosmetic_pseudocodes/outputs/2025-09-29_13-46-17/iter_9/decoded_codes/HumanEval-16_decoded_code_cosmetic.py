from typing import Dict

def count_distinct_characters(input_string: str) -> int:
    index: int = 0
    seen_chars: Dict[str, bool] = {}

    def __recur_count(pos: int, seen: Dict[str, bool]) -> int:
        if pos == len(input_string):
            return 0
        ch: str = input_string[pos].lower()
        if ch not in seen:
            seen[ch] = True
            return 1 + __recur_count(pos + 1, seen)
        else:
            return __recur_count(pos + 1, seen)

    return __recur_count(index, seen_chars)