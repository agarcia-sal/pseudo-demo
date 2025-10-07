def digitSum(string_input: str) -> int:
    if string_input == "":
        return 0
    return sum(ord(c) for c in string_input if c.isupper())