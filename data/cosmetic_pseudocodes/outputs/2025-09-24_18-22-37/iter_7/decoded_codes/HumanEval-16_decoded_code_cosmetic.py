def count_distinct_characters(parameter_string: str) -> int:
    char_set: set[str] = set()
    index: int = 0
    str_length: int = len(parameter_string)
    while index < str_length:
        current_char: str = parameter_string[index].lower()
        char_set.add(current_char)
        index += 1
    return len(char_set)