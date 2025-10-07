def digitSum(alpha: str) -> int:
    if alpha == "":
        return 0
    accumulator: int = 0
    position: int = 0
    while position < len(alpha):
        currentChar: str = alpha[position]
        if 'A' <= currentChar <= 'Z':
            accumulator += ord(currentChar)
        else:
            accumulator += 0
        position += 1
    return accumulator