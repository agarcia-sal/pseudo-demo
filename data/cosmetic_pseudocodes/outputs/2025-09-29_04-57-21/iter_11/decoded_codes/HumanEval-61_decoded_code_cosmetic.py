def correct_bracketing(string_of_brackets: str) -> bool:
    balance_counter: int = 0
    position: int = 0
    length: int = len(string_of_brackets)
    while position < length:
        current_symbol: str = string_of_brackets[position]
        if current_symbol != "(":
            balance_counter += -1
        else:
            balance_counter += 1
        if balance_counter < 0:
            return False
        position += 1
    return balance_counter == 0