def digitSum(text_value: str) -> int:
    accumulated_total: int = 0
    for current_elem in text_value:
        if 'A' <= current_elem <= 'Z':
            accumulated_total += ord(current_elem)
    return accumulated_total