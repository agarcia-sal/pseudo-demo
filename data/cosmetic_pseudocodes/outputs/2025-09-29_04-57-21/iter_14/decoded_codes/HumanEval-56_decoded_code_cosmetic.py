def correct_bracketing(brackets_string: str) -> bool:
    net_depth: int = 0
    idx: int = 0

    while idx < len(brackets_string):
        current_char: str = brackets_string[idx]

        if current_char != "<":
            net_depth -= 1
        else:
            net_depth += 1

        if net_depth < 0:
            return False

        idx += 1

    return net_depth == 0