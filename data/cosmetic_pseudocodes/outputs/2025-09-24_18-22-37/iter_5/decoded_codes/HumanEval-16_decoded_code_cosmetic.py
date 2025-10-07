def count_distinct_characters(str_param: str) -> int:
    char_map: set[str] = set()
    index_counter: int = 1
    str_length: int = len(str_param)
    while index_counter <= str_length:
        current_char: str = str_param[index_counter - 1].lower()
        char_map.add(current_char)
        index_counter += 1
    return len(char_map)