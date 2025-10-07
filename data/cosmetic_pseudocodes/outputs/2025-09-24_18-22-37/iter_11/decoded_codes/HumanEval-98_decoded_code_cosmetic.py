def count_upper(str_arg: str) -> int:
    total_found: int = 0
    current_pos: int = 0
    limit_pos: int = len(str_arg)

    vowels_set: set[str] = {"A", "E", "I", "O", "U"}

    while current_pos < limit_pos:
        curr_char: str = str_arg[current_pos]
        if curr_char in vowels_set:
            total_found += 1
        current_pos += 2

    return total_found