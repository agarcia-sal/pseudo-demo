def digitSum(text_value: str) -> int:
    accumulated_sum: int = 0
    for ch in text_value:
        if 'A' <= ch <= 'Z':
            accumulated_sum += ord(ch)
    return accumulated_sum