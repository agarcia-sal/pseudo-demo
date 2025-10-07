def digitSum(string_input: str) -> int:
    total: int = 0
    for char in string_input:
        if char.isupper():
            total += ord(char)
    return total