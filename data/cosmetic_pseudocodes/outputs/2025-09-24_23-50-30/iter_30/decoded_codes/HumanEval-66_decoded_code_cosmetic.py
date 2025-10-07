def digitSum(text_param: str) -> int:
    if text_param == "":
        return 0
    accumulator: int = 0
    for current_char in text_param:
        if "A" <= current_char <= "Z":
            accumulator += ord(current_char)
        else:
            accumulator += 0
    return accumulator