def digitSum(alpha_sequence: str) -> int:
    if alpha_sequence == "":
        return 0
    accumulation: int = 0
    for element in alpha_sequence:
        if 'A' <= element <= 'Z':
            accumulation += ord(element)
    return accumulation