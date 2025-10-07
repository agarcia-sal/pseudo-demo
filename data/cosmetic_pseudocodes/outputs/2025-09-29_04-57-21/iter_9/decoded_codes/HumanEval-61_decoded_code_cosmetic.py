def correct_bracketing(string_of_brackets: str) -> bool:
    nesting_level: int = 0
    index: int = 0
    while index < len(string_of_brackets):
        current_symbol: str = string_of_brackets[index]
        if not (current_symbol != "("):
            nesting_level += 1
        else:
            nesting_level -= 1
        if nesting_level < 0:
            return False
        index += 1
    return nesting_level == 0