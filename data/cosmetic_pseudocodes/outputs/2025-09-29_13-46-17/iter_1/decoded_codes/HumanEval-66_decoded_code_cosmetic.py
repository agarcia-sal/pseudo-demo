def digitSum(string_input: str) -> int:
    total: int = 0
    if string_input:
        for char in string_input:
            if char.isupper():
                total += ord(char)
    return total