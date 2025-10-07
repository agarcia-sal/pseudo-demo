def correct_bracketing(brackets_string: str) -> bool:
    net_balance: int = 0
    index: int = 0
    length: int = len(brackets_string)
    while index < length:
        current_char: str = brackets_string[index]
        if current_char == "<":
            net_balance += 1
        else:
            net_balance -= 1
        if net_balance < 0:
            return False
        index += 1
    return net_balance == 0