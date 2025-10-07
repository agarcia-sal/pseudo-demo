def digitSum(input_str: str) -> int:
    total: int = 0
    for char in input_str:
        if 'A' <= char <= 'Z':
            total += ord(char)
    return total