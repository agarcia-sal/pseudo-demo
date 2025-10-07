def count_distinct_characters(input_string: str) -> int:
    char_set: set[str] = set()
    idx: int = 0
    str_lower: str = input_string.lower()

    while idx < len(str_lower):
        char_set.add(str_lower[idx])
        idx += 1

    return len(char_set)