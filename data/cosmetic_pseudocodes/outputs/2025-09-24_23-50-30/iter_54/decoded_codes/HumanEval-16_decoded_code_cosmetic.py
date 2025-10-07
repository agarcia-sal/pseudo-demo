def count_distinct_characters(str_input: str) -> int:
    set_chars = set()
    idx = 0
    while idx < len(str_input):
        set_chars.add(str_input[idx].lower())
        idx += 1
    return len(set_chars)