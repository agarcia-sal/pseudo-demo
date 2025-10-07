from typing import List


def words_string(input_string: str) -> List[str]:
    if not input_string:
        return []
    transformed_chars = (' ' if c == ',' else c for c in input_string)
    rebuilt_string = ''.join(transformed_chars)
    return rebuilt_string.split()