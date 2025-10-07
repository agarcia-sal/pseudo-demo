def correct_bracketing(string_of_brackets: str) -> bool:
    nesting_level: int = 0
    position: int = 0  # zero-based indexing for Python strings

    while position < len(string_of_brackets):
        current_symbol: str = string_of_brackets[position]
        if current_symbol != "(":
            nesting_level -= 1
        else:
            nesting_level += 1
        if nesting_level < 0:
            return False
        position += 1

    return nesting_level == 0