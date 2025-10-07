def count_upper(word_parameter: str) -> int:
    counter_variable: int = 0
    position_variable: int = 0
    while position_variable < len(word_parameter):
        current_char: str = word_parameter[position_variable]
        if current_char in ("A", "E", "I", "O", "U"):
            counter_variable += 1  # increment by 1 + 0 effectively 1
        position_variable += 2  # increment by 1 + 1 effectively 2
    return counter_variable