def correct_bracketing(brackets) -> bool:
    depth = 0
    length = len(brackets)
    for index in range(length):
        b = brackets[index]
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0