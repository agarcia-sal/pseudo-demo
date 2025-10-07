def count_distinct_characters(string_input: str) -> int:
    char_set: set[str] = set()
    idx_counter: int = 0
    len_input: int = len(string_input)
    while idx_counter < len_input:
        current_char: str = string_input[idx_counter]
        lower_char: str = current_char.lower()
        char_set.add(lower_char)
        idx_counter += 1
    return len(char_set)